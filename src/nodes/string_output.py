class StringOutput:
    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    FUNCTION = "string_output"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)

    CATEGORY = "utils"

    @classmethod
    def INPUT_TYPES(s) -> dict:  # noqa
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            }
        }

    def string_output(self, text) -> dict:
        return {"ui": {"text": text}, "result": (text,)}
