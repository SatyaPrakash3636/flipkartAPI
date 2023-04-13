import requests
import json
import base64


class Flipkart:
    def __init__(self, api_base_url, auth_base_url, client_id, client_secret) -> None:
        self.api_base_url = api_base_url
        self.auth_base_url = auth_base_url
        self.client_id = client_id
        self.client_secret = client_secret

    def get_token(self):
        url = self.auth_base_url
        client_id = self.client_id
        client_secret = self.client_secret
        credentials = client_id + ":" + client_secret
        credentials_bytes = credentials.encode("ascii")
        b64_credentials_bytes = base64.b64encode(credentials_bytes)
        b64_credentials = b64_credentials_bytes.decode("ascii")
        querystring = {"grant_type": "client_credentials", "scope": "Seller_Api"}
        headers = {"Authorization": "Basic " + b64_credentials}
        resp = requests.get(url, headers=headers, params=querystring)
        # resp = requests.request("GET", url, headers=headers, params=querystring).json()
        return resp.json()

    def get_orders(self, auth_token, orderItemIds):
        # headers = {"Authorization": "Apikey " + auth_token}
        headers = {
            "Authorization": "Bearer " + auth_token,
            "accept": "application/json",
        }
        url = self.api_base_url + f"/v2/orders?orderItemIds={orderItemIds}"

        resp = requests.get(url, headers=headers)
        return resp.json()

    def get_shipments(self, auth_token, orderItemIds):
        headers = {
            "Authorization": "Bearer " + auth_token,
            "accept": "application/json",
        }
        url = self.api_base_url + f"/v2/orders/shipments?orderItemIds={orderItemIds}"

        resp = requests.get(url, headers=headers)
        return resp.json()

    def search_orders(self, auth_token):
        headers = {
            "Authorization": "Bearer " + auth_token,
            "accept": "application/json",
            "Content-Type": "*/*",
        }
        # data = {
        #     "filter": {
        #         "orderDate": {
        #             "from": "2023-02-14T07:49:17.655Z",
        #             "to": "2023-02-15T07:49:17.655Z",
        #         }
        #     }
        # }
        data = {"filter": {}}
        url = self.api_base_url + "/v2/orders/search"

        resp = requests.post(url, headers=headers, data=data)
        return resp.json()

    def get_manifest(self, auth_token):
        headers = {
            "Authorization": "Bearer " + auth_token,
            "accept": "*/*",
        }
        url = self.api_base_url + "/v2/orders/manifest"

        resp = requests.get(url, headers=headers)
        return resp.json()
