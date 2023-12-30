import json
from gzip import compress, decompress

from genie_common.serializers.encoder_interface import IEncoder
from genie_common.typing import Json


class GzipJsonEncoder(IEncoder):
    def encode(self, json_object: Json) -> bytes:
        json_str = json.dumps(json_object)
        json_bytes = json_str.encode("utf-8")

        return compress(json_bytes)

    def decode(self, json_bytes: str) -> Json:
        decompressed_json = decompress(json_bytes)
        json_str = decompressed_json.decode("utf-8")

        return json.loads(json_str)
