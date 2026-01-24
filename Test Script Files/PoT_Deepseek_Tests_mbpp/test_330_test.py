import unittest
from mbpp_330_code import find_char

class TestFindChar(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_char("Hello world"), ['ell', 'o', 'or', 'wor', 'rld'])
        self.assertEqual(find_char("Python is fun"), ['Pyt', 'hon', 'is', 'fun'])

    def test_edge_cases(self):
        self.assertEqual(find_char("a"), [])
        self.assertEqual(find_char(""), [])

    def test_boundary_conditions(self):
        self.assertEqual(find_char("abcdefghijklmnopqrstuvwxyz"), ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'])
        self.assertEqual(find_char("1234567890"), [])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_char(12345)
        with self.assertRaises(TypeError):
            find_char(None)
