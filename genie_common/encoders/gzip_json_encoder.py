import json
from gzip import compress, decompress

from genie_common.consts import UTF_8
from genie_common.encoders.encoder_interface import IEncoder
from genie_common.typing import Json


class GzipJsonEncoder(IEncoder):
    @staticmethod
    def encode(obj: Json) -> bytes:
        json_str = json.dumps(obj)
        json_bytes = json_str.encode(UTF_8)

        return compress(json_bytes)

    @staticmethod
    def decode(obj: bytes) -> Json:
        decompressed_json = decompress(obj)
        json_str = decompressed_json.decode(UTF_8)

        return json.loads(json_str)
