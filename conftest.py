"""pytest configuration file."""

import os
from pytest_readme import setup

setup()

# We move the file test_readme.py from the root directory
# to the tests directory.
os.rename("test_readme.py", "tests/test_readme.py")
