# -*- coding: utf-8 -*-
"""
A thin wrapper of standard ``json`` with standard compression libraries
"""
import json
from typing import Dict

__all__ = [
    "dump",
    "load",
]

_DEFAULT_EXTENSION_MAP = {
    "json": "json",
    "gz": "gzip",
    "bz": "bz2",
    "lzma": "lzma"
}

_DEFAULT_COMPRESSION_WRITE_MODES = {
    "json": r"w",
    "gzip": r"wt",
    "bz2": r"wt",
    "lzma": r"wt"
}

_DEFAULT_COMPRESSION_READ_MODES = {
    "json": r"r",
    "gzip": r"rt",
    "bz2": r"rt",
    "lzma": r"rt"
}


def get_compression_write_mode(compression):
    """Return mode for opening file buffer for writing."""
    return _DEFAULT_COMPRESSION_WRITE_MODES[compression]


def get_compression_read_mode(compression):
    """Return mode for opening file buffer for reading."""
    return _DEFAULT_COMPRESSION_READ_MODES[compression]


def infer_compression_from_filename(filename: str) -> str:
    """Return the compression protocal inferred from given filename.
    Parameters
    ----------
    filename: str
        The filename for which to infer the compression protocol
    """
    return _DEFAULT_EXTENSION_MAP[filename.split(".")[-1]]


def dump(obj, path: str, compression_kwargs: Dict = None, json_kwargs: Dict = None):
    r"""Dump the contents of an object to disk as json, to the supplied path, using the detected compression protocol.
    Parameters
    ----------
    obj: any
        The object that will be saved to disk
    path: str
        The path to the file to which to dump ``obj``
    compression_kwargs:
        keywords argument to pass to the compressed file opening protocol.
    json_kwargs:
        keywords argument to pass to the json file opening protocol.
    """
    compression_kwargs = {} if compression_kwargs is None else compression_kwargs
    json_kwargs = {} if json_kwargs is None else json_kwargs
    compression = infer_compression_from_filename(path)
    mode = get_compression_write_mode(compression)
    if compression is None or compression == "json":
        fout = open(path, mode=mode, **compression_kwargs)
    elif compression == "gzip":
        import gzip

        fout = gzip.open(path, mode=mode, encoding="utf-8", **compression_kwargs)
    elif compression == "bz2":
        import bz2

        fout = bz2.open(path, mode=mode, encoding="utf-8", **compression_kwargs)
    elif compression == "lzma":
        import lzma

        fout = lzma.open(path, mode=mode, encoding="utf-8", **compression_kwargs)
    with fout:
        json.dump(obj, fout, **json_kwargs)


def load(path: str, compression_kwargs: Dict = None, json_kwargs: Dict = None):
    r"""Return json object at given path uncompressed with detected compression protocol.
    Parameters
    ----------
    path: str
        The path to the file from which to load the ``obj``
    compression_kwargs:
        keywords argument to pass to the compressed file opening protocol.
    json_kwargs:
        keywords argument to pass to the json file opening protocol.
    """
    compression_kwargs = {} if compression_kwargs is None else compression_kwargs
    json_kwargs = {} if json_kwargs is None else json_kwargs
    compression = infer_compression_from_filename(path)
    mode = get_compression_read_mode(compression)
    if compression is None or compression == "json":
        file = open(path, mode=mode, **compression_kwargs)
    elif compression == "gzip":
        import gzip
        file = gzip.open(path, mode=mode, encoding="utf-8", **compression_kwargs)
    elif compression == "bz2":
        import bz2
        file = bz2.open(path, mode=mode, encoding="utf-8", **compression_kwargs)
    elif compression == "lzma":
        import lzma
        file = lzma.open(path, mode=mode, encoding="utf-8", **compression_kwargs)
    with file:
        return json.load(file, **json_kwargs)
