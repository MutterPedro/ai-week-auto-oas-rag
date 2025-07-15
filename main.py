import os
import asyncio
import logging

from app.rag_auto_oas import RAGAutoOAS
from app.samples.royal_mail import ROYAL_MAIL_REQUEST, ROYAL_MAIL_RESPONSE

# Configure logging to display in terminal
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()  # This ensures logs go to console/terminal
    ]
)

log = logging.getLogger(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

async def main():
    # List of available models
    # for model in openai.models.list():
    #     print(model.id)
        
    auto_oas = RAGAutoOAS(api_key=OPENAI_API_KEY)
    auto_oas.display_graph("./results/workflow_graph.png")
    result = auto_oas.generate_spec(ROYAL_MAIL_REQUEST, ROYAL_MAIL_RESPONSE)

    # log.info(f"Schema cache: {auto_oas.schema_cache}")
    # log.info(f"Auth patterns: {auto_oas.auth_patterns}")

    with open("./results/result.yml", "w") as f:
        result = result.replace("```yaml", "").replace("```", "").strip()
        f.write(result)

if __name__ == "__main__":
    asyncio.run(main())