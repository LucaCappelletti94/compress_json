"""Test that file extensions are handled case-insensitively."""

import compress_json
from compress_json.compress_json import infer_compression_from_filename


def test_infer_compression_ignores_extension_case():
    assert infer_compression_from_filename("data.json") == "json"
    assert infer_compression_from_filename("data.JSON") == "json"
    assert infer_compression_from_filename("data.Gz") == "gzip"
    assert infer_compression_from_filename("data.BZ") == "bz2"
    assert infer_compression_from_filename("archive.tar.LZMA") == "lzma"
    assert infer_compression_from_filename("data.Xz") == "lzma"


def test_dump_and_load_with_uppercase_extension(tmp_path):
    """Round-trip through dump/load with an uppercase extension."""
    path = str(tmp_path / "object.JSON")
    compress_json.dump({"hello": "world"}, path)
    assert compress_json.load(path) == {"hello": "world"}
