import os
import logging

from libs.sdks.python import MutterpedroApi

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

log = logging.getLogger(__name__)

def test_sdk():
    PARTNER_TOKEN = os.getenv("PARTNER_TOKEN", "")


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
    test_sdk()