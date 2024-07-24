# compress_json

[![pip](https://badge.fury.io/py/compress-json.svg)](https://pypi.org/project/compress-json/)
[![python](https://img.shields.io/pypi/pyversions/compress-json.svg)](https://pypi.org/project/compress-json/)
[![license](https://img.shields.io/pypi/l/compress-json.svg)](https://pypi.org/project/compress-json/)
[![downloads](https://pepy.tech/badge/compress-json)](https://pepy.tech/project/compress-json)
[![Github Actions](https://github.com/LucaCappelletti94/ugly_csv_generator/actions/workflows/python.yml/badge.svg)](https://github.com/LucaCappelletti94/ugly_csv_generator/actions/)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/6aa4b62b4ed34f7d8e2c37ef09848294)](https://app.codacy.com/gh/LucaCappelletti94/compress_json/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

The missing Python utility to read and write large compressed JSONs.

The library is loosely based on the [compress_pickle](https://github.com/lucianopaz/compress_pickle) library.

## How do I install this package?

As usual, just download it using pip:

```shell
pip install compress_json
```

## Available compression modes

The compression modes, detected automatically by the file name, are **gzip**, **bz2**, and **lzma**, with the notable exception of **zip** which seems difficult to integrate into the JSON pipeline.

## Usage example

The library is extremely easy to use:

```python
import compress_json

D = {
    "A": {
        "B": "C"
    }
}
compress_json.dump(D, "filepath.json.gz")   # for a gzip file
compress_json.dump(D, "filepath.json.bz")   # for a bz2 file
compress_json.dump(D, "filepath.json.lzma") # for a lzma file

D1 = compress_json.load("filepath.json.gz")   # for loading a gzip file
D2 = compress_json.load("filepath.json.bz")   # for loading a bz2 file
D3 = compress_json.load("filepath.json.lzma") # for loading a lzma file
```

If it happens that you have to load a file with some custom extension that is actually a compressed JSON file, you can specify the compression mode manually:

```python
import compress_json

D1 = compress_json.load("filepath.custom_extension", compression="gzip")   # for loading a gzip file
D2 = compress_json.load("filepath.custom_extension", compression="bz2")   # for loading a bz2 file
D3 = compress_json.load("filepath.custom_extension", compression="lzma") # for loading a lzma file
```

Analogously, you can specify the compression mode when dumping a JSON object when the file extension is not one of the standard ones:

```python
import compress_json

D = {
    "A": {
        "B": "C"
    }
}

compress_json.dump(D, "filepath.custom_extension", compression="gzip")   # for a gzip file
compress_json.dump(D, "filepath.custom_extension", compression="bz2")   # for a bz2 file
compress_json.dump(D, "filepath.custom_extension", compression="lzma") # for a lzma file
```

## Some extra perks: local loading and dumping

The library makes available, other than the usual `load` and `dump` from the JSON library, the methods `local_load` and `local_dump`, which let you load and dump files in the same directory as wherever you are calling them, by using the call stack.

This can be useful, especially when loading files within packages.

```python
import compress_json

D = {
    "A": {
        "B": "C"
    }
}
compress_json.local_dump(D, "filepath.json.gz")   # for a gzip file
compress_json.local_dump(D, "filepath.json.bz")   # for a bz2 file
compress_json.local_dump(D, "filepath.json.lzma") # for a lzma file

D1 = compress_json.local_load("filepath.json.gz")   # for loading a gzip file
D2 = compress_json.local_load("filepath.json.bz")   # for loading a bz2 file
D3 = compress_json.local_load("filepath.json.lzma") # for loading a lzma file
```

## Loading with RAM cache

Sometimes you need to load a compressed JSON file a LOT of times, and you may want to put this document in a cache or something of the sort. Fortunately, we already provide this option for you:

```python
import compress_json

D1 = compress_json.load(
    "filepath.json.gz",
    use_cache=True
)

D1 = compress_json.local_load(
    "filepath.json.gz",
    use_cache=True
)
```

## Advanced usage

You can pass parameters to either the chosen compression mode or the JSON library.

With the `json_kwargs` parameter, you can specify any of the kwargs that should be forwarded to the JSON library method, which you can obtain for your Python version by running `help(json.dump)` and `help(json.load)`, depending on whether you are dumping or loading the JSON object.

Similarly, with the `compression_kwargs` parameter, you can specify any parameter that has to be forwarded to the compression library that you intend to use, whether that is `lzma`, `gzip`, or `bz2`, and as per JSON will depend on which version you have installed.

Whether you are dumping or loading a compressed JSON object, you can get the list of parameters you have available to forward to the compression method by running `help(lzma.open)`, `help(gzip.open)`, or `help(bz2.open)`, respectively.

```python
import compress_json

D = {
    "A": {
        "B": "C"
    }
}
compress_json.dump(
    D, "filepath.json.gz",
    compression_kwargs={kwargs go here},
    json_kwargs={kwargs go here}
)

D4 = compress_json.load(
    "filepath.json.gz",
    compression_kwargs={kwargs go here},
    json_kwargs={kwargs go here}
)
```