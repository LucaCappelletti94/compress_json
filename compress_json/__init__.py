"""Compress JSON is a package to handle reading and writing of compressed JSON documents."""
from .compress_json import load, dump, local_load, local_dump
from support_developer import support_luca

support_luca("compress_json")

__all__ = ["load", "dump", "local_load", "local_dump"]
