import compress_json
import os
import shutil
from random_dict import random_dict
from dict_hash import sha256


def test_compress_json():
    D = random_dict(10, 10)
    key = sha256(D)
    extensions = compress_json.compress_json._DEFAULT_EXTENSION_MAP.keys()
    for ext in extensions:
        path = f"random_dirs/test.json.{ext}"
        compress_json.dump(D, path)
        assert key == sha256(compress_json.load(path))
    
    shutil.rmtree("random_dirs")

    for ext in extensions:
        path = f"random_dirs/test.json.{ext}"
        compress_json.local_dump(D, path)
        assert key == sha256(compress_json.local_load(path))
    
    shutil.rmtree("tests/random_dirs")