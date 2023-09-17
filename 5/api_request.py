class ApiRequest:
    def __init__(self, request_type, payload) -> None:
        self._request_type = request_type
        self._payload = payload
    
    def set_payload(self, payload):
        self._payload = payload

    def get_payload(self):
        return self._payload