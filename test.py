from flipkartAPI.flipkartAPI import Flipkart
from flipkartAPI.utility import *
from flipkartAPI.constant import API_BASE_URL, AUTH_BASE_URL, CLIENT_SECRET, CLIENT_ID


API_BASE_URL = API_BASE_URL
AUTH_BASE_URL = AUTH_BASE_URL
CLIENT_ID = CLIENT_ID
CLIENT_SECRET = CLIENT_SECRET

davcare = Flipkart(API_BASE_URL, AUTH_BASE_URL, CLIENT_ID, CLIENT_SECRET)

response_json = davcare.get_token()
auth_token = response_json["access_token"]
print(response_json)
print(auth_token)
response_json = davcare.search_orders(auth_token)
print(json.dumps(response_json, indent=4))

# response_json = davcare.get_orders(auth_token, "327304085464557100")
# print(json.dumps(response_json, indent=4))
