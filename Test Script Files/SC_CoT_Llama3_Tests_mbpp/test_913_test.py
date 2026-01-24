import unittest
from mbpp_913_code import end_num

class TestEndNum(unittest.TestCase):
    def test_typical_input(self):
        self.assertTrue(end_num("hello123"))
        self.assertTrue(end_num("world456"))

    def test_edge_case(self):
        self.assertTrue(end_num("abcdefg9"))
        self.assertTrue(end_num("hijklmn0"))

    def test_boundary_case(self):
        self.assertTrue(end_num("hello"))
        self.assertTrue(end_num("123456"))

    def test_empty_string(self):
        self.assertFalse(end_num(""))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            end_num(123)

    def test_no_digit(self):
        self.assertFalse(end_num("hello world"))

    def test_multiple_digits(self):
        self.assertTrue(end_num("hello12345"))

    def test_single_digit(self):
        self.assertTrue(end_num("hello1"))

    def test_multiple_digits_at_end(self):
        self.assertTrue(end_num("helloabc123"))

    def test_single_digit_at_end(self):
        self.assertTrue(end_num("helloabc1"))
