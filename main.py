import json
import os
import asyncio
import logging

from app.rag_auto_oas import RAGAutoOAS
from app.samples.royal_mail import ROYAL_MAIL_REQUEST, ROYAL_MAIL_RESPONSE

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

log = logging.getLogger(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
PARTNER_TOKEN = os.getenv("PARTNER_TOKEN", "")

async def main():
    # List of available models
    # for model in openai.models.list():
    #     print(model.id)
        
    auto_oas = RAGAutoOAS(api_key=OPENAI_API_KEY)
    auto_oas.display_graph("./results/workflow_graph.png")
    result = auto_oas.generate_spec(ROYAL_MAIL_REQUEST, ROYAL_MAIL_RESPONSE)

    with open("./results/result.yml", "w") as f:
        result = result.replace("```yaml", "").replace("```", "").strip()
        f.write(result)

def main_sdk_example():
    from libs.sdks.python import MutterpedroApi

    client = MutterpedroApi(
        base_url="https://api.clickanddrop.royalmail.com",
        partner_token=PARTNER_TOKEN,
        api_key="1234567890"
    )

    response = client.shipping_services.get_shipping_services(
        country="GBR",
        weight="1000"
    )

    # print the response in pretty format
    log.info(response.json(indent=2))

if __name__ == "__main__":
    asyncio.run(main())
    # main_sdk_example()