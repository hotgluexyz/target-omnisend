from singer_sdk import typing as th
from target_hotglue.target import TargetHotglue

from target_omnisend.sinks import (
    ContactsSink,
)


class TargetOmniSend(TargetHotglue):
    name = "target-omnisend"
    SINK_TYPES = [ContactsSink]
    MAX_PARALLELISM = 1

    config_jsonschema = th.PropertiesList(
        th.Property("api_key", th.StringType, required=True),
    ).to_dict()


if __name__ == "__main__":
    TargetOmniSend.cli()
