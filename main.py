import json
import os
import asyncio
import logging
import openai

from app.auto_oas import AutoOAS
from app.samples.royal_mail import ROYAL_MAIL_REQUEST, ROYAL_MAIL_RESPONSE


log = logging.getLogger(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

async def main():
    # List of available models
    # for model in openai.models.list():
    #     print(model.id)
        
    auto_oas = AutoOAS(api_key=OPENAI_API_KEY)
    result = await auto_oas.analyze_request_response(ROYAL_MAIL_REQUEST, ROYAL_MAIL_RESPONSE)

    # log.info(f"Schema cache: {auto_oas.schema_cache}")
    # log.info(f"Auth patterns: {auto_oas.auth_patterns}")

    with open("./results/result.yml", "w") as f:
        result = result.replace("```yaml", "").replace("```", "").strip()
        f.write(result)

if __name__ == "__main__":
    asyncio.run(main())