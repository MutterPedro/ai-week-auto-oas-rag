import json
import logging
import openai

from app.utils.errors import SchemaInferenceError

log = logging.getLogger(__name__)

class AutoOAS:
    def __init__(self, api_key: str):
        openai.api_key = api_key
        self.schema_cache = {}
        self.auth_patterns = {}


    async def _infer_schema(self, response: dict, endpoint_info: str, auth_info: str) -> str:
        """Infer OpenAPI schema from response data"""
        prompt = f"""
        Infer OpenAPI schema from JSON response:
        
        The response body content is:
        {json.dumps(response["body"], indent=2)}
        
        Generate a complete OpenAPI schema definition including:
        - Type definitions
        - Required fields
        - Format specifications
        - Example values
        
        Format as valid OpenAPI 3.0 schema.
        Do not add any new elements, parameters, fields, or response codes not present in the original fragments.
        """
        
        try:
            completion = openai.chat.completions.create(
                model="gpt-4.1",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.9,
                max_tokens=2048 * 4,
            )

            content = completion.choices[0].message.content
            if content is None:
                return ""

            prompt = f"""
            Task: Merge the provided OpenAPI YAML fragments into a single, valid OpenAPI 3.0 specification.

            Constraints:
            - The output must be a single, complete, and valid OpenAPI 3.0 specification in YAML format.
            - Preserve every detail from the source fragments, especially all fields, descriptions, and response objects.
            - Do not add any new elements, parameters, fields, or response codes not present in the original fragments.
            - Your response must contain only the final YAML code, without any extra text, explanations, or markdown formatting.
            - Example values must honor what is defined as schemas in the original fragments.

            Response content:
            {content}

            The endpoint information is:
            {endpoint_info}

            The authentication information is:
            {auth_info}
            """
            
            completion = openai.chat.completions.create(
                model="gpt-4.1",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.9,
                max_tokens=2048 * 10,
            )
            
            self.schema_cache[hash(json.dumps(response))] = completion.choices[0].message.content
            return completion.choices[0].message.content or ""
            
        except Exception as e:
            raise SchemaInferenceError(f"Failed to infer schema: {str(e)}")

    async def _detect_auth_patterns(self, request: dict) -> str:
        """Detect authentication patterns in HTTP request"""
        prompt = f"""
        Analyze authentication patterns in HTTP request:
        Method: {request['method']}
        Headers: {json.dumps(request.get('headers', {}), indent=2)}
        URL: {request['url']}
        
        Identify:
        1. Authentication scheme (OAuth2, Basic Auth, API Key, etc.)
        2. Authentication flow
        3. Required credentials
        4. Security scopes
        5. Generate solely the authentication scheme in OpenAPI security scheme definition in YAML format.
        """
        
        completion = openai.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=2048
        )
        
        auth_scheme = completion.choices[0].message.content
        if auth_scheme is None:
            return ""
        
        self.auth_patterns[request['url']] = auth_scheme

        return auth_scheme

    async def _analyze_endpoint(self, request: dict, response: dict) -> str:
        """Analyze endpoint characteristics"""
        prompt = f"""
        Analyze endpoint characteristics:
        Request:
        Method: {request['method']}
        URL: {request['url']}
        Headers: {json.dumps(request.get('headers', {}), indent=2)}
        Body: {json.dumps(request.get('body', ''), indent=2)}
        
        Response:
        Status: {response['status_code']}
        
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
        """
        
        completion = openai.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=2048
        )
        
        content = completion.choices[0].message.content
        if content is None:
            return ""
        
        return content

    async def analyze_request_response(self, request: dict, response: dict) -> str:
        """Analyze HTTP request/response pair and generate OpenAPI components"""
        # Generate schema for response

        # Detect authentication patterns
        print(f"Detecting authentication patterns for {request['url']}")
        auth_info = await self._detect_auth_patterns(request)
        print(f"Authentication patterns: {auth_info}")
        
        # Analyze endpoint characteristics
        print(f"Analyzing endpoint characteristics for {request['url']}")
        endpoint_info = await self._analyze_endpoint(request, response)
        print(f"Endpoint characteristics: {endpoint_info}")

        # Infer schema
        print(f"Inferring schema for {request['url']}")
        schema = await self._infer_schema(response, endpoint_info, auth_info)
        
        return schema