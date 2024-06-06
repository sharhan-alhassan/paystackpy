import os

"""
This script defines constants used across the Paystackpy codebase.

Constants:
    SECRET_KEY (str): The Paystack secret key used for authentication.
                      This key is retrieved from the environment variable `PAYSTACK_SECRET_KEY`.
                      If the environment variable is not set, `SECRET_KEY` will be `None`.

    HEADERS (dict): A dictionary containing the authorization header required for Paystack API requests.
                    The value of the 'Authorization' key is a string formatted with a Bearer token.
                    This token should be replaced with the actual secret key at runtime.

    BASE_API_URL (str): The base URL for Paystack API requests.
                        All API endpoints will be appended to this base URL.
"""

# The Paystack secret key used for authentication
# This key is retrieved from the environment variable `PAYSTACK_SECRET_KEY`
# If the environment variable is not set, `SECRET_KEY` will be `None`
SECRET_KEY = os.getenv("PAYSTACK_SECRET_KEY", None)

# A dictionary containing the authorization header required for Paystack API requests
# The value of the 'Authorization' key is a string formatted with a Bearer token
# This token should be replaced with the actual secret key at runtime
HEADERS = {'Authorization': 'Bearer {}'}

# The base URL for Paystack API requests
# All API endpoints will be appended to this base URL
BASE_API_URL = 'https://api.paystack.co/'
