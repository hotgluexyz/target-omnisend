from target_hotglue.client import HotglueSink
from target_hotglue.auth import Authenticator

class OmnisendApiKeyAuthenticator(Authenticator):

    @property
    def auth_headers(self):
        return {"X-API-KEY": self._config.get("api_key")}


class OmnisendSink(HotglueSink):

    @property
    def base_url(self) -> str:
        return self.config.get("url", "https://api.omnisend.com/v5")

    @property
    def authenticator(self):
        return OmnisendApiKeyAuthenticator(self._target)
