import requests
from typing import List
from config import BFF_URL, APPTUS_CONF, FYNDIQ_URL


class FyndiqBff:
    def search(keywords: List[str]) -> list:
        url = BFF_URL.format(query=" ".join(keywords[:3]))
        response = requests.get(url, headers=APPTUS_CONF)
        products = response.json()["productListWithCount"]["articles"][:10]
        return [
            dict(
                url=f'{FYNDIQ_URL}{product["article_url"]}',
                image_url=product["images"][0]["url"],
            )
            for product in products
        ]
