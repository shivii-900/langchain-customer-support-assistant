import os
from dotenv import load_dotenv

load_dotenv()


MAX_CUSTOMER_QUERY_LENGTH = int(
    os.getenv("MAX_CUSTOMER_QUERY_LENGTH", "4000")
)
