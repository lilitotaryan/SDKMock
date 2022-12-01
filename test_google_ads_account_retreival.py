from get_google_accounts import extract_data_from_pagination_object
from mock import MockGoogleAdsData

CUSTOMER_ACCOUNT_DATA = [
    {
        "customer_client": {
            "resource_name": "customers/60411050567/customerClients/2210121194",
            "descriptive_name": "Google_RDC",
            "id": 60411050567,
        }
    },
    {
        "customer_client": {
            "resource_name": "customers/6041105078/customerClients/2210121185",
            "descriptive_name": "Google_RDC1",
            "id": 6041105078,
        }
    },
]


def test_extract_data_from_google_pagination_object_manager_accounts():
    result = extract_data_from_pagination_object(
        MockGoogleAdsData(CUSTOMER_ACCOUNT_DATA)
    )
    assert result[0]["parent_name"][0] == "Google_RDC"
    assert result[0]["parent_id"][0] == 60411050567
    assert result[1]["parent_name"][1] == "Google_RDC1"
    assert result[1]["parent_id"][1] == 6041105078

