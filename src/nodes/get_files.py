import os


class GetFiles:
    CATEGORY = "utils"
    FUNCTION = "get_files"
    OUTPUT_NODE = True
    RETURN_TYPES = ("STRING",)

    @classmethod
    def INPUT_TYPES(cls) -> dict:  # noqa
        return {
            "required":{
                "dir_path": ("STRING", {"default": "input"}),
            }
        }

    @classmethod
    def VALIDATE_INPUTS(cls, dir_path) -> bool | str: # noqa
        if not os.path.exists(dir_path):
            return f"No such directory {dir_path}"

        return True

    def get_files(self, dir_path: str) -> str:
        files = "\n".join(sorted(os.listdir(dir_path)))

        return {"ui": {"text": (files,)}, "result": (files,)}
