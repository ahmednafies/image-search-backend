import os
from dotenv import load_dotenv

load_dotenv()

BFF_URL = "https://search-bff.fyndiq.se/search/result?{query}"
FYNDIQ_URL = "https://fyndiq.se"
APPTUS_CONF = {
    "apptus-customerkey": os.environ["APPTUS_CUSTOMER_KEY"],
    "apptus-market": os.environ["APPTUS_MARKET"],
    "apptus-sessionkey": os.environ["APPTUS_SESSION_KEY"],
}
