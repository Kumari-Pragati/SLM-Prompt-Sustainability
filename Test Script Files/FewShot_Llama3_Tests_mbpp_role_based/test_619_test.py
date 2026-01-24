import unittest
from mbpp_619_code import move_num

class TestMoveNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(move_num("hello123world"), "hello123world")

    def test_edge_case_empty_string(self):
        self.assertEqual(move_num(""), "")

    def test_edge_case_single_digit(self):
        self.assertEqual(move_num("a1b"), "a1b")

    def test_edge_case_single_non_digit(self):
        self.assertEqual(move_num("a"), "a")

    def test_edge_case_multiple_digits(self):
        self.assertEqual(move_num("abc123def"), "abc123def")

    def test_edge_case_multiple_non_digits(self):
        self.assertEqual(move_num("abcdef"), "abcdef")

    def test_edge_case_mixed_digits_and_non_digits(self):
        self.assertEqual(move_num("abc123def456"), "abc123def456")
