# -*- coding: utf-8 -*-
"""
A thin wrapper of standard ``json`` with standard compression libraries.
"""
import json
from typing import Dict, Any, Optional
import traceback
import os

__all__ = [
    "dump",
    "load",
    "local_dump",
    "local_load"
]

_DEFAULT_EXTENSION_MAP = {
    "json": "json",
    "gz": "gzip",
    "bz": "bz2",
    "lzma": "lzma"
}

_DEFAULT_COMPRESSION_WRITE_MODES = {
    "json": "w",
    "gzip": "wt",
    "bz2": "wt",
    "lzma": "wt"
}

_DEFAULT_COMPRESSION_READ_MODES = {
    "json": "r",
    "gzip": "rt",
    "bz2": "rt",
    "lzma": "rt"
}

_CACHE = {}


def get_compression_write_mode(compression: str) -> str:
    """Return mode for opening file buffer for writing.

    Parameters
    -------------------
    compression: str
        The extension of the compression to be used.

    Returns
    -------------------
    The code to use for opening the file in write mode.
    """
    return _DEFAULT_COMPRESSION_WRITE_MODES[compression]


def get_compression_read_mode(compression: str) -> str:
    """Return mode for opening file buffer for reading.

    Parameters
    -------------------
    compression: str
        The extension of the compression to be used.

    Returns
    -------------------
    The code to use for opening the file in read mode.
    """
    return _DEFAULT_COMPRESSION_READ_MODES[compression]


def infer_compression_from_filename(filename: str) -> str:
    """Return the compression protocal inferred from given filename.

    Parameters
    ----------
    filename: str
        The filename for which to infer the compression protocol
    """
    return _DEFAULT_EXTENSION_MAP[filename.split(".")[-1]]


def dump(
    obj: Any,
    path: str,
    compression_kwargs: Optional[Dict] = None,
    json_kwargs: Optional[Dict] = None
):
    """Dump the contents of an object to disk as json using the detected compression protocol.

    Parameters
    ----------------
    obj: any
        The object that will be saved to disk
    path: str
        The path to the file to which to dump ``obj``
    compression_kwargs: Optional[Dict] = None
        Keywords argument to pass to the compressed file opening protocol.
    json_kwargs: Optional[Dict] = None
        Keywords argument to pass to the json file opening protocol.

    Raises
    ----------------
    ValueError
        If given path is not a valid string.
    """
    if not isinstance(path, str):
        if isinstance(obj, str):
            raise ValueError(
                (
                    "The object you have provided to the dump method is a string "
                    "while the object you have provided as a path is NOT a string "
                    "but an object of type {}. Maybe you need to swap them?"
                ).format(type(path))
            )
        raise ValueError("The given path is not a string.")
    compression_kwargs = {} if compression_kwargs is None else compression_kwargs
    json_kwargs = {} if json_kwargs is None else json_kwargs
    compression = infer_compression_from_filename(path)
    mode = get_compression_write_mode(compression)

    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    if compression is None or compression == "json":
        fout = open(path, mode=mode, encoding="utf-8", **compression_kwargs)
    elif compression == "gzip":
        import gzip

        fout = gzip.open(path, mode=mode, encoding="utf-8",
                         **compression_kwargs)
    elif compression == "bz2":
        import bz2

        fout = bz2.open(path, mode=mode, encoding="utf-8",
                        **compression_kwargs)
    elif compression == "lzma":
        import lzma

        fout = lzma.open(path, mode=mode, encoding="utf-8",
                         **compression_kwargs)
    with fout:
        json.dump(obj, fout, **json_kwargs)


def load(
    path: str,
    compression_kwargs: Optional[Dict] = None,
    json_kwargs: Optional[Dict] = None,
    use_cache: bool = False
):
    """Return json object at given path uncompressed with detected compression protocol.

    Parameters
    ----------
    path: str
        The path to the file from which to load the ``obj``
    compression_kwargs: Optional[Dict] = None
        keywords argument to pass to the compressed file opening protocol.
    json_kwargs: Optional[Dict] = None
        keywords argument to pass to the json file opening protocol.
    use_cache: bool = False
        Whether to put loaded JSON files in a static cache object.

    Raises
    ----------------
    ValueError
        If given path is not a valid string.
    """
    if not isinstance(path, str):
        raise ValueError("The given path is not a string.")

    if use_cache and path in _CACHE:
        return _CACHE[path]

    compression_kwargs = {} if compression_kwargs is None else compression_kwargs
    json_kwargs = {} if json_kwargs is None else json_kwargs
    compression = infer_compression_from_filename(path)
    mode = get_compression_read_mode(compression)
    if compression is None or compression == "json":
        file = open(path, mode=mode, encoding="utf-8", **compression_kwargs)
    elif compression == "gzip":
        import gzip
        file = gzip.open(path, mode=mode, encoding="utf-8",
                         **compression_kwargs)
    elif compression == "bz2":
        import bz2
        file = bz2.open(path, mode=mode, encoding="utf-8",
                        **compression_kwargs)
    elif compression == "lzma":
        import lzma
        file = lzma.open(path, mode=mode, encoding="utf-8",
                         **compression_kwargs)
    with file:
        json_content = json.load(file, **json_kwargs)

    if use_cache:
        _CACHE[path] = json_content
    
    return json_content


def local_path(relative_path: str) -> str:
    """Return path localized to caller function.

    Parameters
    -----------------------
    relative_path: str
        The path to be made absolute to the caller function.

    Returns
    -----------------------
    The absolute path with as root the caller function.
    """
    return os.path.join(
        os.path.dirname(
            os.path.abspath(
                traceback.extract_stack()[-3].filename
            )
        ),
        relative_path
    )


def local_load(
    path: str,
    compression_kwargs: Optional[Dict] = None,
    json_kwargs: Optional[Dict] = None,
    use_cache: bool = False
) -> Any:
    """Return json object at given local path uncompressed with detected compression protocol.

    Parameters
    ----------
    path: str
        The path to the local file from which to load the ``obj``
    compression_kwargs: Optional[Dict] = None
        keywords argument to pass to the compressed file opening protocol.
    json_kwargs: Optional[Dict] = None
        keywords argument to pass to the json file opening protocol.
    use_cache: bool = False
        Whether to put loaded JSON files in a static cache object.

    Raises
    ----------------
    ValueError,
        If given path is not a valid string.
    """
    return load(
        local_path(path),
        compression_kwargs,
        json_kwargs,
        use_cache
    )


def local_dump(
    obj: Any,
    path: str,
    compression_kwargs: Optional[Dict] = None,
    json_kwargs: Optional[Dict] = None
):
    """Dump the contents of an object to disk as json, using the detected compression protocol.

    Parameters
    ----------
    obj: Any
        The object that will be saved to disk
    path: str
        The local path to the file to which to dump ``obj``
    compression_kwargs: Optional[Dict] = None
        keywords argument to pass to the compressed file opening protocol.
    json_kwargs: Optional[Dict] = None
        keywords argument to pass to the json file opening protocol.

    Raises
    ----------------
    ValueError
        If given path is not a valid string.
    """
    dump(obj, local_path(path), compression_kwargs, json_kwargs)
