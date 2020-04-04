compress_json
=========================================================================================
|travis| |sonar_quality| |sonar_maintainability| |codacy| |code_climate_maintainability| |pip| |downloads|

Python package that handles loading and dumping JSON files in a compressed fashion. The library is loosely based on the `compress_pickle <https://github.com/lucianopaz/compress_pickle>`_ library.

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install compress_json

Tests Coverage
----------------------------------------------
Since some software handling coverages sometimes
get slightly different results, here's three of them:

|coveralls| |sonar_coverage| |code_climate_coverage|

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


Som extra perks
----------------------------------------------
The library makes available, other than the usual load and dump from the
JSON library, also the methods load_load and local_dump which let you
load and dump file in the same directory of wherever you are calling them,
by using the call stack.

This can get useful expecially when loading files within packages.

.. code:: python

    import compress_json
    
    D = {
        "A":{
            "B":"C"
        }
    }
    compress_json.local_dump(D, "filepath.json.gz") # for a gzip file
    compress_json.local_dump(D, "filepath.json.bz") # for a bz2 file
    compress_json.local_dump(D, "filepath.json.lzma") # for a lzma file

    D1 = compress_json.local_load("filepath.json.gz") # for loading a gzip file
    D2 = compress_json.local_load("filepath.json.bz") # for loading a bz2 file
    D3 = compress_json.local_load("filepath.json.lzma") # for loading a lzma file

Advanced usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Clearly you can pass parameters to either the chosen compression mode or the json library as follows:

.. code:: python

    import compress_json
    
    D = {
        "A":{
            "B":"C"
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

.. |travis| image:: https://travis-ci.org/LucaCappelletti94/compress_json.png
   :target: https://travis-ci.org/LucaCappelletti94/compress_json
   :alt: Travis CI build

.. |sonar_quality| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_compress_json&metric=alert_status
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_compress_json
    :alt: SonarCloud Quality

.. |sonar_maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_compress_json&metric=sqale_rating
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_compress_json
    :alt: SonarCloud Maintainability

.. |sonar_coverage| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_compress_json&metric=coverage
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_compress_json
    :alt: SonarCloud Coverage

.. |coveralls| image:: https://coveralls.io/repos/github/LucaCappelletti94/compress_json/badge.svg?branch=master
    :target: https://coveralls.io/github/LucaCappelletti94/compress_json?branch=master
    :alt: Coveralls Coverage

.. |pip| image:: https://badge.fury.io/py/compress-json.svg
    :target: https://badge.fury.io/py/compress-json
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/compress-json
    :target: https://pepy.tech/badge/compress-json
    :alt: Pypi total project downloads 

.. |codacy|  image:: https://api.codacy.com/project/badge/Grade/6aa4b62b4ed34f7d8e2c37ef09848294
    :target: https://www.codacy.com/manual/LucaCappelletti94/compress_json?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LucaCappelletti94/compress_json&amp;utm_campaign=Badge_Grade
    :alt: Codacy Maintainability

.. |code_climate_maintainability| image:: https://api.codeclimate.com/v1/badges/c79ec561e2fd2b91763c/maintainability
    :target: https://codeclimate.com/github/LucaCappelletti94/compress_json/maintainability
    :alt: Maintainability

.. |code_climate_coverage| image:: https://api.codeclimate.com/v1/badges/c79ec561e2fd2b91763c/test_coverage
    :target: https://codeclimate.com/github/LucaCappelletti94/compress_json/test_coverage
    :alt: Code Climate Coverate