from google.ads.googleads.client import GoogleAdsClient


def extract_data_from_pagination_object(response):
    data = []
    for batch in response:
        for row in batch.results:
            data_row = {
                "parent_name": row.customer_client.descriptive_name,
                "parent_id": row.customer_client.id,
            }
            data.append(data_row)
    return data


def get_data(client, customer_id, accounts):
    ga_service = client.get_service("GoogleAdsService")
    search_request = client.get_type("SearchGoogleAdsStreamRequest")
    search_request.customer_id = customer_id
    search_request.query = f"""
SELECT
customer_client.descriptive_name,
customer.id,
customer_client.id,
customer_client.manager
FROM customer_client
WHERE customer_client.manager = TRUE
  and customer_client.id in {accounts}"""
    response = ga_service.search_stream(search_request)
    data = extract_data_from_pagination_object(response)
    return data


def get_account_data():
    secrets = {
            "developer_token": "developer_token",
            "client_id": "client_id",
            "client_secret": "client_secret",
            "refresh_token": "refresh_token",
            "login_customer_id": "login_customer_id",
            "use_proto_plus": False}

    google_ads_client = GoogleAdsClient.load_from_dict(
        version="v10", config_dict=secrets
    )

    accounts = ["1", "2", "3", "4"]
    return get_data(google_ads_client, secrets["login_customer_id"], accounts)
