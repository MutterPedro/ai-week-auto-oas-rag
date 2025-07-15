# AI Week OAS Generator

A Proof of Concept (PoC) for automatically generating OpenAPI specifications using LangGraph and RAG (Retrieval Augmented Generation). This project demonstrates how to create accurate API specifications from sample requests and responses, then generate SDKs using Fern.

## What This Project Does

- **Generates OpenAPI specs**: Uses AI techniques with LangGraph framework and RAG to analyze API request/response pairs and automatically generate comprehensive OpenAPI specifications
- **Creates SDKs**: Leverages Fern to generate type-safe SDKs from the generated OpenAPI specs

## Project Structure

```
ai-week-oas-generator/
├── app/                    # Main application logic
│   ├── rag_auto_oas.py    # Core RAG-based OpenAPI generation
│   ├── auto_oas.py        # Base OpenAPI generation logic
│   └── samples/           # API samples for testing
│       └── royal_mail.py  # Royal Mail API sample data
├── libs/
│   ├── fern/              # Fern configuration
│   └── sdks/python/       # Generated Python SDK
├── main.py                # Main entry point and examples
├── requirements.txt       # Python dependencies
└── results/               # Generated outputs
```

## Setup Instructions

### 1. Activate Virtual Environment

```bash
# Activate the existing virtual environment
pythom -m venv venv
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Variables

Set up your environment variables:

```bash
export OPENAI_API_KEY="your-openai-api-key"
export PARTNER_TOKEN="your-partner-token"  # For Royal Mail API example
```

## Usage

### Generate OpenAPI Specification

Run the main script to generate an OpenAPI spec from the Royal Mail sample:

```bash
python main.py
```

This will:

- Generate an OpenAPI specification using RAG
- Save the result to `./results/result.yml`
- Create a workflow visualization at `./results/workflow_graph.png`

### Adding New Samples

To add new API samples for OpenAPI generation:

1. Create a new file in `app/samples/` (e.g., `app/samples/your_api.py`)
2. Define your request and response examples:

```python
YOUR_API_REQUEST = {
    "method": "GET",
    "url": "https://api.example.com/endpoint",
    "headers": {
        "Authorization": "Bearer token"
    },
    "params": {
        "param1": "value1"
    }
}

YOUR_API_RESPONSE = {
    "status_code": 200,
    "headers": {
        "Content-Type": "application/json"
    },
    "body": {
        "data": "example response"
    }
}
```

3. Import and use in `main.py`:

```python
from app.samples.your_api import YOUR_API_REQUEST, YOUR_API_RESPONSE

# In main function:
result = auto_oas.generate_spec(YOUR_API_REQUEST, YOUR_API_RESPONSE)
```

### Generate SDK using Fern

To generate SDKs from your OpenAPI specification using Fern:

1. **Install Fern CLI**: Follow the [Fern Quick Start Guide](https://docs.buildwithfern.com/learn/quickstart)

2. **Update Fern Configuration**: Modify `libs/fern/fern.config.json` and `libs/fern/generators.yml` as needed

3. **Generate SDK**:
   ```bash
   cd libs
   fern generate
   ```

For detailed Fern setup and configuration, refer to the [official Fern documentation](https://docs.buildwithfern.com/).

### Run SDK Example

To test the generated SDK with a real API:

1. **Uncomment the SDK example** in `main.py`:

   ```python
   if __name__ == "__main__":
       # asyncio.run(main())  # Comment this out
       main_sdk_example()     # Uncomment this
   ```

2. **Run the example**:
   ```bash
   python main.py
   ```

This will demonstrate how to use the generated Python SDK to make API calls.

## Requirements

- Python 3.8+
- OpenAI API key
- Dependencies listed in `requirements.txt`

## Output Files

- `./results/result.yml`: Generated OpenAPI specification
- `./results/workflow_graph.png`: Visualization of the generation workflow
- `libs/sdks/python/`: Generated Python SDK files
