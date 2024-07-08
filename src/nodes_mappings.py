from .nodes.format_string import FormatString
from .nodes.get_files import GetFiles
from .nodes.load_image_by_path import LoadImageByPath

NODE_CLASS_MAPPINGS = {
    "LoadImageByPath": LoadImageByPath,
    "GetFiles": GetFiles,
    "FormatString": FormatString,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadImageByPath": "Load Image By Path",
    "GetFiles": "Get Files",
    "FormatString": "Format String",
}

