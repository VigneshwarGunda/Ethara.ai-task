class Login:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def send_creds(self):
        username = self.username  # capture here

        class DummyResponse:
            status_code = 200

            def json(self):
                return {
                    "access_token": "dummy_token",
                    "role": "Admin",   # IMPORTANT (matches condition)
                    "username": username
                }

        return DummyResponse()