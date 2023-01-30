compress_json
=========================================================================================
|pip| |downloads|

The missing Python utility to read and write large compressed JSONs.

The library is loosely based on the :code:`compress_pickle <https://github.com/lucianopaz/compress_pickle>`_ library.

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install compress_json

Available compression modes
----------------------------------------------
The compression modes, detected automatically by the file name, are **gzip**, **bz2** and **lzma**,
with the notable exception of **zip** which seems difficult to integrate in the JSON pipeline.

Usage example
----------------------------------------------
The library is extremely easy to use:

.. code:: python

    import compress_json
    
    D = {
        "A":{
            "B":"C"
        }
    }
    compress_json.dump(D, "filepath.json.gz") # for a gzip file
    compress_json.dump(D, "filepath.json.bz") # for a bz2 file
    compress_json.dump(D, "filepath.json.lzma") # for a lzma file

    D1 = compress_json.load("filepath.json.gz") # for loading a gzip file
    D2 = compress_json.load("filepath.json.bz") # for loading a bz2 file
    D3 = compress_json.load("filepath.json.lzma") # for loading a lzma file


Some extra perks: local loading and dumping
----------------------------------------------
The library makes available, other than the usual load and dump from the JSON library, the methods local_load and local_dump, which let you load and dump file in the same directory of wherever you are calling them, by using the call stack.

This can get useful, especially when loading files within packages.

.. code:: python

    import compress_json
    
    D = {
        "A": {
            "B": "C"
        }
    }
    compress_json.local_dump(D, "filepath.json.gz") # for a gzip file
    compress_json.local_dump(D, "filepath.json.bz") # for a bz2 file
    compress_json.local_dump(D, "filepath.json.lzma") # for a lzma file

    D1 = compress_json.local_load("filepath.json.gz") # for loading a gzip file
    D2 = compress_json.local_load("filepath.json.bz") # for loading a bz2 file
    D3 = compress_json.local_load("filepath.json.lzma") # for loading a lzma file

Loading with RAM cache
----------------------------------------------
Sometimes you need to load a compressed JSON file a LOT of times, and you may want to
put this document in a cache or something of the sorts. Fortunately, we already provide
this option for you:

.. code:: python

    import compress_json
    
    D1 = compress_json.load(
        "filepath.json.gz",
        use_cache=True
    )

    D1 = compress_json.local_load(
        "filepath.json.gz",
        use_cache=True
    )

Advanced usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can pass parameters to either the chosen compression mode or the JSON library.

With the :code:`json_kwargs` parameter you can specify any of the kwargs that should
be forwarded to the JSON library method, which you can obtain for your Python version
by running :code:`help(json.dump)` and :code:`help(json.load)`, depending whether you are
dumping or loading the json object.

Analogously, with the :code:`compression_kwargs` parameter you can specify any parameter that
has to be forwarded to the compression library that you intend to use, whether that is
`lzma`, :code:`gzip` or :code:`bz2`, and as per JSON will depend on which version you have installed.

Whether you are dumping or loading a compressed JSON object, you can get the list of parameters you
have available to forward to the compression method by running :code:`help(lzma.open)`, :code:`help(gzip.open)`
or :code:`help(bz2.open)`, respectively.

.. code:: python

    import compress_json
    
    D = {
        "A": {
            "B": "C"
        }
    }
    compress_json.dump(
        D, "filepath.json.gz",
        compression_kwargs = {kwargs go here},
        json_kwargs = {kwargs go here}
    )

    D4 = compress_json.load(
        "filepath.json.gz",
        compression_kwargs = {kwargs go here},
        json_kwargs = {kwargs go here}
    )


.. |pip| image:: https://badge.fury.io/py/compress-json.svg
    :target: https://badge.fury.io/py/compress-json
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/compress-json
    :target: https://pepy.tech/badge/compress-json
    :alt: Pypi total project downloads 
