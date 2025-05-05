from target_omnisend.client import OmnisendSink

class ContactsSink(OmnisendSink):
    name = "contacts"
    endpoint = "/contacts"
    batch = None

    def preprocess_record(self, record: dict, context: dict) -> dict:
        return record

    def upsert_record(self, record: dict, context: dict):
        state_updates = {}

        try:
            response = self.request_api(
                "POST", endpoint=self.endpoint, request_data=record
            )

            if response.ok:
                self.logger.info(f"Successfully posted contact")
                result = response.json()
                return result.get("contactID"), True, state_updates
            else:
                self.logger.error(f"Failed to post contact: {response.text}")
                return None, False, {"error": f"{response.status_code} - {response.text}"}
        except Exception as e:
            self.logger.error(f"Failed to post contact: {str(e)}")
            return None, False, {"error": str(e)}


class EventsSink(OmnisendSink):
    name = "events"
    endpoint = "/events"
    batch = None

    def preprocess_record(self, record: dict, context: dict) -> dict:
        return record

    def upsert_record(self, record: dict, context: dict):
        state_updates = {}

        try:
            response = self.request_api(
                "POST", endpoint=self.endpoint, request_data=record
            )

            if response.ok:
                self.logger.info(f"Successfully posted event")
                return None, True, state_updates
            else:
                self.logger.error(f"Failed to post event: {response.text}")
                return None, False, {"error": f"{response.status_code} - {response.text}"}
        except Exception as e:
            self.logger.error(f"Failed to post event: {str(e)}")
            return None, False, {"error": str(e)}
