import pytest
from api_request import ApiRequest

class TestApiRequest:
    def test_constructor(self):
        request = ApiRequest("GET", {"param1": "value1", "param2": "value2"})
        assert request._request_type == "GET"
        assert request._payload == {"param1": "value1", "param2": "value2"}

    def test_set_payload(self):
        request = ApiRequest("GET", {"param1": "value1", "param2": "value2"})
        request.set_payload({"new_param": "new_value"})
        assert request._payload == {"new_param": "new_value"}

    def test_get_payload(self):
        request = ApiRequest("GET", {"param1": "value1", "param2": "value2"})
        assert request._payload == request.get_payload()