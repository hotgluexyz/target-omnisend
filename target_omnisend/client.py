from target_hotglue.client import HotglueSink


class OmnisendApiKeyAuthenticator:
    def __init__(self, target, api_key) -> None:
        self.target_name: str = target.name
        self.api_key = api_key

    @property
    def auth_headers(self):
        return {"X-API-KEY": self.api_key}


class OmnisendSink(HotglueSink):

    @property
    def base_url(self) -> str:
        return self.config.get("url", "https://api.omnisend.com/v5")

    @property
    def authenticator(self):
        return OmnisendApiKeyAuthenticator(self._target, self.config.get("api_key"))
