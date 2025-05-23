from singer_sdk import typing as th
from target_hotglue.target import TargetHotglue

from target_omnisend.sinks import (
    ContactsSink,
    EventsSink,
)


class TargetOmnisend(TargetHotglue):
    name = "target-omnisend"
    SINK_TYPES = [ContactsSink, EventsSink]
    MAX_PARALLELISM = 1

    config_jsonschema = th.PropertiesList(
        th.Property("api_key", th.StringType, required=True),
    ).to_dict()


if __name__ == "__main__":
    TargetOmnisend.cli()
