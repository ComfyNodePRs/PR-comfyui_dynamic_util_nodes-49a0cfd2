import hashlib
import os

import numpy as np
import torch
from PIL import Image, ImageOps


class LoadImageByPath:
    CATEGORY = "image"
    RETURN_TYPES = ("IMAGE", "MASK")
    FUNCTION = "load_image_by_path"

    @classmethod
    def INPUT_TYPES(cls) -> dict:  # noqa
        return {
            "required":{
                "img_pth": ("STRING", {"default": "input/example.png"}),
            }
        }

    @classmethod
    def VALIDATE_INPUTS(cls, image_path) -> bool | str: # noqa
        if not os.path.exists(image_path) and not os.path.isfile(image_path):
            return "Invalid image file: {}".format(image_path)

        return True

    @classmethod
    def IS_CHANGED(cls, image_path: str) -> str:  # noqa
        m = hashlib.sha256()
        with open(image_path, 'rb') as f:
            m.update(f.read())

        return m.digest().hex()

    def load_image(self, image_path: str) -> tuple[torch.Tensor, torch.Tensor]:
        img = Image.open(image_path)
        img = ImageOps.exif_transpose(img)

        if img.mode == 'I':
            img = img.point(lambda i: i * (1 / 255))

        img = img.convert("RGB")
        img = np.array(img).astype(np.float32) / 255.0
        img = torch.from_numpy(img)[None,]

        if 'A' in img.getbands():
            mask = np.array(img.getchannel('A')).astype(np.float32) / 255.0
            mask = 1. - torch.from_numpy(mask)
        else:
            mask = torch.zeros((64,64), dtype=torch.float32, device="cpu")

        return img, mask
