import requests
from config import BFF_URL, APPTUS_CONF, FYNDIQ_URL


class FyndiqBff:
    def search(keyword):
        url = BFF_URL.format(query=keyword)
        response = requests.get(url, headers=APPTUS_CONF)
        products = response.json()["productListWithCount"]["articles"][:4]
        return [
            dict(
                url=f'{FYNDIQ_URL}{product["article_url"]}',
                image_url=product["images"][0]["url"],
            )
            for product in products
        ]
