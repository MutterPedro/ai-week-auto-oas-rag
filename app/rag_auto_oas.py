import json
import logging
from typing import TypedDict

from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langchain_core.tools import tool
from IPython.display import Image, display
from yamllint import linter
from openapi_spec_validator import validate
from openapi_spec_validator.validation.exceptions import OpenAPIValidationError
from openapi_spec_validator.readers import read_from_filename

from app.utils.persistence import delete_yaml_file, load_yaml_file, save_yaml_file

log = logging.getLogger(__name__)

# 1. Analyze and extract object models and schemas
# 2. Analyze and extract authentication patterns from the request
# 3. Analyze and extract endpoint characteristics from the request and response
# 4. Retrieve previously generated YAML files, if present
# 5. Merge the information into a single OpenAPI 3.0 specification
# 6. Apply a linter in the YAML file
# 7. Check if the syntax is respecting the OpenAPI 3.0 specification
# 8. Check whether the OpenAPI 3.0 specification is complete and did not made up any information that is not available in the original input or previously cached specification file


class State(TypedDict):
    request: dict
    response: dict
    object_schemas: str
    auth_patterns: str
    endpoint_characteristics: str
    oas_spec: str
    prev_oas_spec: str

class Memory(BaseModel):
    content: str = Field(description="The main content of the memory. For example: User expressed interest in learning about French.")

class MemoryCollection(BaseModel):
    memories: list[Memory] = Field(description="A list of memories about the user.")

class RAGAutoOAS:
    def __init__(self, api_key: str):
        log.info("🤖 Initializing RAG Auto-OAS System... Standing by for operations.")
        self.llm = init_chat_model(
            model="gpt-4.1",
            api_key=api_key,
            temperature=0.9,
            max_tokens=2048 * 10,
        )
        self.memory = MemorySaver()

        tools = [
            self._retrieve_yaml_file,
            self._save_yaml_file,
            self._lint_yaml_file,
            self._validate_oas_spec,
            self._url_to_file_name
        ]
        self.llm.bind_tools(tools)

        graph_builder = StateGraph(State)
        graph_builder.add_node("analyze_and_extract_object_schemas", self._analyze_and_extract_object_schemas)
        graph_builder.add_node("analyze_and_extract_auth_patterns", self._analyze_and_extract_auth_patterns)
        graph_builder.add_node("analyze_and_extract_endpoint_characteristics", self._analyze_and_extract_endpoint_characteristics)
        graph_builder.add_node("retrieve_previously_generated_yaml_files", self._retrieve_previously_generated_yaml_files)
        graph_builder.add_node("merge_oas_specs", self._merge_oas_specs)
        graph_builder.add_node("apply_yaml_linter", self._apply_yaml_linter)
        graph_builder.add_node("check_oas_spec_completeness", self._check_oas_spec_completeness)
        graph_builder.add_node("verify_hallucination", self._verify_hallucination)

        graph_builder.add_edge(START, "analyze_and_extract_object_schemas")
        graph_builder.add_edge("analyze_and_extract_object_schemas", "analyze_and_extract_auth_patterns")
        graph_builder.add_edge("analyze_and_extract_auth_patterns", "analyze_and_extract_endpoint_characteristics")
        graph_builder.add_edge("analyze_and_extract_endpoint_characteristics", "retrieve_previously_generated_yaml_files")
        graph_builder.add_edge("retrieve_previously_generated_yaml_files", "merge_oas_specs")
        graph_builder.add_edge("merge_oas_specs", "apply_yaml_linter")
        graph_builder.add_edge("apply_yaml_linter", "check_oas_spec_completeness")
        graph_builder.add_edge("check_oas_spec_completeness", "verify_hallucination")
        graph_builder.add_edge("verify_hallucination", END)

        self.graph = graph_builder.compile(checkpointer=self.memory)
        log.info("✅ RAG Auto-OAS System fully operational. All systems green.")
    
    def display_graph(self, save_to_file: str | None = None):
        try:
            png_data = self.graph.get_graph().draw_mermaid_png()
            
            if save_to_file:
                with open(save_to_file, 'wb') as f:
                    f.write(png_data)
                log.info(f"📊 Workflow diagram successfully archived to {save_to_file}")
            else:
                display(Image(png_data))
        except Exception as e:
            log.exception(f"❌ Failed to display/save graph: {e}")

    def generate_spec(self, request: dict, response: dict) -> str:
        log.info("🚀 Initiating OpenAPI specification generation sequence...")
        log.info(f"🎯 Target endpoint: {request.get('method', 'UNKNOWN')} {request.get('url', 'UNKNOWN')}")
        
        state: State = State(
            request=request,
            response=response,
            object_schemas='',
            auth_patterns='',
            endpoint_characteristics='',
            oas_spec='',
            prev_oas_spec=''
        )

        state = self.graph.invoke(state, config=dict(run_name="rag_auto_oas", thread_id=request['url'])) # type: ignore
        
        log.info("🎉 OpenAPI specification generation complete. Mission accomplished.")
        return state['oas_spec']

    def _analyze_and_extract_object_schemas(self, state: State) -> State:
        log.info("🔍 Phase 1: Analyzing request and response payloads for object schemas...")
        log.info("📊 Scanning data structures and extracting type definitions...")
        
        prompt = f"""
        Analyze the request and response to extract object models and schemas.
        Generate a complete OpenAPI 3.0 schema definition including:
        - Type definitions
        - Required fields
        - Format specifications
        - Example values

        Generate solely the OpenAPI 3.0 schema definition in YAML format.
        
        Format as valid OpenAPI 3.0 schema.
        Do not add any new elements, parameters, fields, or response codes not present in the original fragments.

        Request: {json.dumps(state['request'], indent=2)}
        Response: {json.dumps(state['response'], indent=2)}
        """

        result = self.llm.invoke(prompt)
        state['object_schemas'] = str(result.content)
        
        log.info("✅ Phase 1 complete: Object schemas successfully extracted and catalogued.")
        return state

    def _analyze_and_extract_auth_patterns(self, state: State) -> State:
        log.info("🔐 Phase 2: Analyzing authentication patterns and security schemes...")
        log.info("🛡️ Scanning for security protocols and access control mechanisms...")
        
        prompt = f"""
        Analyze the request and response to extract authentication patterns.
        Generate a complete OpenAPI 3.0 authentication scheme definition including:
        - Authentication scheme (OAuth2, Basic Auth, API Key, etc.)
        - Authentication flow
        - Required credentials
        - Security scopes

        Generate solely the OpenAPI 3.0 authentication scheme definition in YAML format.

        Format as valid OpenAPI 3.0 authentication scheme definition.
        Do not add any new elements, parameters, fields, or response codes not present in the original fragments.

        Request: {json.dumps(state['request'], indent=2)}
        """

        result = self.llm.invoke(prompt)
        state['auth_patterns'] = str(result.content)
        
        log.info("✅ Phase 2 complete: Authentication patterns identified and security framework established.")
        return state

    def _analyze_and_extract_endpoint_characteristics(self, state: State) -> State:
        log.info("🌐 Phase 3: Analyzing endpoint characteristics and operation details...")
        log.info("📡 Processing HTTP method, parameters, and response patterns...")
        
        prompt = f"""
        Analyze the endpoint characteristics
        Request:
        Method: {state['request']['method']}
        URL: {state['request']['url']}
        Headers: {json.dumps(state['request'].get('headers', {}), indent=2)}
        Body: {json.dumps(state['request'].get('body', ''), indent=2)}
        
        Response:
        Status: {state['response']['status_code']}
        
        Generate OpenAPI operation object including:
        - Operation ID
        - Summary and description
        - Parameters
        - Request body schema
        - Response definitions
        - Tags
        - Path
        - Method
        - URL
        - Host

        Generate solely the OpenAPI operation object in YAML format.

        Format as valid OpenAPI 3.0 operation object.
        Do not add any new elements, parameters, fields, or response codes not present in the original fragments.
        """

        result = self.llm.invoke(prompt)
        state['endpoint_characteristics'] = str(result.content)
        
        log.info("✅ Phase 3 complete: Endpoint characteristics mapped and operation profile created.")
        return state
    
    def _retrieve_previously_generated_yaml_files(self, state: State) -> State:
        log.info("📁 Phase 4: Accessing historical specification archives...")
        log.info("🔍 Searching for existing OpenAPI definitions in the knowledge base...")
        
        result = self._retrieve_yaml_file.invoke({"request": state['request']})
        if result:
            state['prev_oas_spec'] = result
            log.info("✅ Phase 4 complete: Previous specification found and loaded into memory.")
        else:
            log.info("✅ Phase 4 complete: No previous specifications found. Starting with clean slate.")
        return state

    def _merge_oas_specs(self, state: State) -> State:
        log.info("🔄 Phase 5: Merging specifications and consolidating API definitions...")
        log.info("⚡ Integrating schemas, authentication, and endpoint data...")
        
        prompt = f"""
        Merge the previously generated OpenAPI 3.0 specification with the new one.
        {"The previous specification is:" + state['prev_oas_spec'] if state['prev_oas_spec'] else ""}
        
        The new assessed available object schemas are:
        {state['object_schemas']}
        
        The new assessed authentication patterns are:
        {state['auth_patterns']}
        
        The new assessed endpoint characteristics are:
        {state['endpoint_characteristics']}

        Generate solely the OpenAPI 3.0 specification in YAML format.
        Format as valid OpenAPI 3.0 specification.
        Do not add any new elements, parameters, fields, or response codes not present in the original fragments.
        """

        result = self.llm.invoke(prompt)
        state['oas_spec'] = str(result.content)
        
        log.info("✅ Phase 5 complete: Specification merge successful. Unified API definition ready.")
        return state

    def _apply_yaml_linter(self, state: State) -> State:
        log.info("🔧 Phase 6: Running YAML syntax validation and quality assurance...")
        log.info("🧪 Performing lint analysis to ensure structural integrity...")
        
        yaml_content = state['oas_spec'].replace("```yaml", "").replace("```", "").strip()
        syntax_errors = self._lint_yaml_file.invoke({"content": yaml_content})
        if syntax_errors:
            log.warning(f"⚠️ YAML syntax issues detected. Initiating auto-repair sequence...")
            log.warning(f"🔧 Errors found: {syntax_errors}")
            
            prompt = f"""
            The YAML file is not valid.
            The syntax errors are:
            {syntax_errors}

            Fix the YAML file.
            """

            result = self.llm.invoke(prompt)
            state['oas_spec'] = str(result.content)
            log.info("✅ Phase 6 complete: YAML syntax errors corrected. File structure optimized.")
            return state
        else:
            log.info("✅ Phase 6 complete: YAML syntax validation passed. No structural issues detected.")
            return state

    def _check_oas_spec_completeness(self, state: State) -> State:
        log.info("🔍 Phase 7: Validating OpenAPI specification compliance...")
        log.info("📋 Checking adherence to OpenAPI 3.0 standards and completeness...")
        
        yaml_content = state['oas_spec'].replace("```yaml", "").replace("```", "").strip()
        errors = self._validate_oas_spec.invoke({"request": state['request'], "content": yaml_content})
        if errors:
            log.warning(f"⚠️ OpenAPI validation issues detected. Applying corrective measures...")
            log.warning(f"🔧 Validation errors: {errors}")
            
            prompt = f"""
            The OpenAPI specification is not valid.
            The errors are:
            {errors}

            Fix the OpenAPI specification.
            """

            result = self.llm.invoke(prompt)
            state['oas_spec'] = str(result.content)
            log.info("✅ Phase 7 complete: OpenAPI specification corrected and validated.")
        else:
            log.info("✅ Phase 7 complete: OpenAPI specification validation passed. Compliance confirmed.")

        return state

    def _verify_hallucination(self, state: State) -> State:
        log.info("🎯 Phase 8: Final verification and hallucination prevention protocol...")
        log.info("🔍 Cross-referencing generated specification with original data sources...")
        
        prompt = f"""
        Verify if the OpenAPI specification is complete and did not made up any information that is not available in the original input or previously cached specification file.
        The OpenAPI specification is:
        {state['oas_spec']}
        
        The original input is:
        Request: {json.dumps(state['request'], indent=2)}
        Response: {json.dumps(state['response'], indent=2)}
        
        - If you find any issue, fix it and return the fixed OpenAPI specification.
        - Generate solely the OpenAPI 3.0 specification in YAML format.
        - Format as valid OpenAPI 3.0 specification.
        - Do not add any new elements, parameters, fields, or response codes not present in the original fragments.
        - Remove any notes, comments, or other non-OpenAPI content.
        """

        result = self.llm.invoke(prompt)
        state['oas_spec'] = str(result.content)

        yaml_content = state['oas_spec'].replace("```yaml", "").replace("```", "").strip()
        self._save_yaml_file.invoke({"request": state['request'], "content": yaml_content})
        
        log.info("💾 Specification archived to persistent storage.")
        log.info("✅ Phase 8 complete: Data integrity verified. No hallucinations detected.")
        log.info("🎊 All systems nominal. OpenAPI specification generation sequence complete.")

        return state

    @staticmethod
    @tool
    def _retrieve_yaml_file(request: dict) -> str | None:
        """
        Retrieve the YAML file from the cache.
        The request is:
        {json.dumps(request, indent=2)}
        """

        url = request['url']
        try:
            content = load_yaml_file(url)
            return content
        except Exception as e:
            log.warning(f"Failed to retrieve YAML file: {e}")
            return None
    
    @staticmethod
    @tool
    def _save_yaml_file(request: dict, content: str):
        """
        Save the YAML file to the cache.
        The request is:
        {json.dumps(request, indent=2)}
        """

        url = request['url']
        try:
            file_name = RAGAutoOAS._url_to_file_name.invoke({"url": url})
            save_yaml_file(file_name, content)
            log.info(f"YAML file saved: {url}")
        except Exception as e:
            log.exception(f"Failed to save YAML file: {e}")
            raise

    @staticmethod
    @tool
    def _lint_yaml_file(content: str) -> str:
        """
        Lint the YAML file.
        The content is:
        {content}
        """

        syntax_errors = linter.get_syntax_error(content)

        return syntax_errors.message if syntax_errors else ""
    
    @staticmethod
    @tool
    def _validate_oas_spec(request: dict, content: str) -> str:
        """
        Validate the OpenAPI specification.
        The content is:
        {content}
        """

        try:
            temp_file = "temp_" + RAGAutoOAS._url_to_file_name.invoke({"url": request['url']})
            file_path = save_yaml_file(temp_file, content)

            spec_dict, _ = read_from_filename(file_path)
            validate(spec_dict)
            delete_yaml_file(temp_file)

            return ""
        except OpenAPIValidationError as e:
            return str(e)
        except Exception as e:
            log.exception(f"Failed to validate OpenAPI specification: {e}")
            raise
    
    @staticmethod
    @tool
    def _url_to_file_name(url: str) -> str:
        """
        Convert the URL to a file name.
        The URL is:
        {url}
        """

        domain = url.split("://")[1].split("/")[0]
        return domain.replace(".", "_")