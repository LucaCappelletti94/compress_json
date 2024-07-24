"""Compress JSON is a package to handle reading and writing of compressed JSON documents."""

from compress_json.compress_json import (
    load,
    dump,
    local_load,
    local_dump,
    get_supported_extensions,
)

__all__ = ["load", "dump", "local_load", "local_dump", "get_supported_extensions"]
