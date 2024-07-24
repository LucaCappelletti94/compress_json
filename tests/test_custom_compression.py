"""Submodule to test custom extension for compression algorithms."""
import os
import compress_json


def test_custom_compression():
    """Test custom extension for compression algorithms."""
    D = {
        "A": {
            "B": "C"
        }
    }

    compress_json.dump(D, "filepath.custom_extension1", compression="gzip")   # for a gzip file
    compress_json.dump(D, "filepath.custom_extension2", compression="bz2")   # for a bz2 file
    compress_json.dump(D, "filepath.custom_extension3", compression="lzma") # for a lzma file

    assert compress_json.load("filepath.custom_extension1", compression="gzip") == D
    assert compress_json.load("filepath.custom_extension2", compression="bz2") == D
    assert compress_json.load("filepath.custom_extension3", compression="lzma") == D

    os.remove("filepath.custom_extension1")
    os.remove("filepath.custom_extension2")
    os.remove("filepath.custom_extension3")

   # We test analogously for local_dump and local_load

    compress_json.local_dump(D, "filepath.custom_extension1", compression="gzip")   # for a gzip file
    compress_json.local_dump(D, "filepath.custom_extension2", compression="bz2")   # for a bz2 file
    compress_json.local_dump(D, "filepath.custom_extension3", compression="lzma") # for a lzma file

    assert compress_json.local_load("filepath.custom_extension1", compression="gzip") == D
    assert compress_json.local_load("filepath.custom_extension2", compression="bz2") == D
    assert compress_json.local_load("filepath.custom_extension3", compression="lzma") == D

    os.remove("tests/filepath.custom_extension1")
    os.remove("tests/filepath.custom_extension2")
    os.remove("tests/filepath.custom_extension3") 