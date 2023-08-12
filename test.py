#!/usr/bin/env python
import ctypes
import getpass
import os
import sys
import subprocess
import pytest
import platform
import shutil
import warnings
from string import Template

medir = os.path.realpath(os.path.dirname(__file__))
pardir = os.path.realpath(os.path.join(medir, os.pardir, os.pardir))
if pardir not in sys.path:
    sys.path.insert(0, pardir)

if sys.hexversion < 0x02070000:
    import unittest2 as unittest
else:
    import unittest


class testHotfix(unittest.TestCase):
    pass


def create_big_test(a, b, c):
    def test_big(self):
        # here is ok to use a, b and c ...
        assert(True)
    return test_big

test_method = create_big_test("x", "y", "z")
test_method.__name__ = 'test_x'
setattr(testHotfix, test_method.__name__, test_method)

if __name__ == "__main__":
    unittest.main()