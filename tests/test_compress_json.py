"""Tests whether all compression algorithms work on a random dictionary imput."""
import shutil

from dict_hash import sha256
from random_dict import random_string_dict
import compress_json


def test_compress_json():
    """Tests whether all compression algorithms work on a random dictionary imput."""
    dictionary = random_string_dict(10, 10)
    key = sha256(dictionary)
    extensions = compress_json.compress_json._DEFAULT_EXTENSION_MAP.keys()
    for ext in extensions:
        path = f"random_dirs/test.json.{ext}"
        compress_json.dump(dictionary, path)
        assert key == sha256(compress_json.load(path))
        assert key == sha256(compress_json.load(path, use_cache=True))

    shutil.rmtree("random_dirs")

    for ext in extensions:
        path = f"random_dirs/test.json.{ext}"
        compress_json.local_dump(dictionary, path)
        assert key == sha256(compress_json.local_load(path))
        assert key == sha256(compress_json.local_load(path, use_cache=True))

    shutil.rmtree("tests/random_dirs")
