class FormatString:
    CATEGORY = "utils"
    FUNCTION = "format_string"
    INPUT_NODE = True
    OUTPUT_NODE = True
    RETURN_TYPES = ("STRING",)

    @classmethod
    def INPUT_TYPES(cls) -> dict:  # noqa
        return {
            "required":{
                "string": ("STRING", {"default": "Hello {var}", "forceInput": True}),
                "var": ("STRING", {"default": "var"}),
                "val": ("STRING", {"default": "world"}),
            }
        }

    def format_string(self, string: str, var: str, val: str) -> str:
        result = string.format(**{var: val})

        return {"ui": {"text": (result,)}, "result": (result,)}

