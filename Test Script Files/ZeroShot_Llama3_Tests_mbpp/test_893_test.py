import unittest
from mbpp_893_code import Extract

class TestExtract(unittest.TestCase):

    def test_extract(self):
        self.assertEqual(Extract(['abc', 'def', 'ghi']), ['c', 'f', 'i'])
        self.assertEqual(Extract(['123', '456', '789']), ['3', '6', '9'])
        self.assertEqual(Extract(['hello', 'world', 'python']), ['o', 'r', 'n'])
        self.assertEqual(Extract([]), [])
        self.assertEqual(Extract(['abc']), ['c'])

    def test_extract_empty_list(self):
        self.assertEqual(Extract([]), [])
