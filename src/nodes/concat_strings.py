from typing import Any


class ConcatStrings:
    CATEGORY = "utils"
    FUNCTION = "concat_strings"
    INPUT_NODE = True
    OUTPUT_NODE = True
    RETURN_TYPES = ("STRING",)

    @classmethod
    def INPUT_TYPES(cls) -> dict:  # noqa
        return {
            "required": {
                "string_a": ("STRING", {"default": "", "forceInput": True}),
                "string_b": ("STRING", {"default": "", "forceInput": True}),
            },
            "hidden": {"id_": "UNIQUE_ID"},
        }

    def concat_strings(self, string_a: str, string_b: str, id_: Any) -> str:
        result = "\n".join([string_a, string_b])

        return {"ui": {"text": (result,)}, "result": (result,)}
