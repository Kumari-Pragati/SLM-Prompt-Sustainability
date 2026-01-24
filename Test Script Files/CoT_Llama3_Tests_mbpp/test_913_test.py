import unittest
from mbpp_913_code import end_num

class TestEndNum(unittest.TestCase):
    def test_typical_strings(self):
        self.assertTrue(end_num("hello123"))
        self.assertTrue(end_num("world456"))
        self.assertTrue(end_num("python789"))

    def test_edge_cases(self):
        self.assertTrue(end_num("hello"))
        self.assertTrue(end_num("123456"))
        self.assertTrue(end_num("hello123456"))

    def test_empty_string(self):
        self.assertFalse(end_num(""))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            end_num(123)

    def test_non_matching_strings(self):
        self.assertFalse(end_num("hello world"))
        self.assertFalse(end_num("abc def"))
