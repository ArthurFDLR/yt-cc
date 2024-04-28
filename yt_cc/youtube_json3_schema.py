from .logger import logger

from jsonschema import validate, ValidationError, SchemaError


def validate_youtube_cc_json3(json_data):
    try:
        validate(json_data, _YOUTUBE_CC_JSON3_SCHEMA)
    except ValidationError as e:
        logger.warning(f"Validation Error: {e.message}")
        return False
    except SchemaError as e:
        logger.warning(f"Schema Error: {e.message}")
        return False
    return True


_YOUTUBE_CC_JSON3_SCHEMA = {
    "$schema": "http://json-schema.org/schema#",
    "title": "Youtube's CC JSON3 Schema",
    "description": "Schema for the JSON3 closed captions files from Youtube",
    "type": "object",
    "properties": {
        "wireMagic": {"type": "string"},
        "pens": {
            "type": "array",
            "items": {"type": "object", "properties": {"iAttr": {"type": "integer"}}},
        },
        "wsWinStyles": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "mhModeHint": {"type": "integer"},
                    "juJustifCode": {"type": "integer"},
                    "sdScrollDir": {"type": "integer"},
                },
            },
        },
        "wpWinPositions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "apPoint": {"type": "integer"},
                    "ahHorPos": {"type": "integer"},
                    "avVerPos": {"type": "integer"},
                    "rcRows": {"type": "integer"},
                    "ccCols": {"type": "integer"},
                },
            },
        },
        "events": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "tStartMs": {"type": "integer"},
                    "dDurationMs": {"type": "integer"},
                    "id": {"type": "integer"},
                    "wpWinPosId": {"type": "integer"},
                    "wsWinStyleId": {"type": "integer"},
                    "wWinId": {"type": "integer"},
                    "segs": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "utf8": {"type": "string"},
                                "acAsrConf": {"type": "integer"},
                                "tOffsetMs": {"type": "integer"},
                                "pPenId": {"type": "integer"},
                            },
                            "required": ["utf8"],
                        },
                    },
                    "aAppend": {"type": "integer"},
                },
                "required": ["tStartMs"],
            },
        },
    },
    "required": ["events", "pens", "wireMagic", "wpWinPositions", "wsWinStyles"],
}
