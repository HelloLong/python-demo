import sys

import unittest

print('sys.path')
# print('sys.path', sys.path)
# from foo import bar
from foo.bar import dumb_true

class TestBar(unittest.TestCase):
    def test_bar_true(self):
        self.assertTrue(dumb_true)
        # self.assertFalse(bar.dumb_true)

if __name__ == "__main__":
    unittest.main()