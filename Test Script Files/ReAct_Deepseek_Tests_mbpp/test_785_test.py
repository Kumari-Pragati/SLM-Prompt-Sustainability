import unittest
from mbpp_785_code import tuple_str_int

class TestTupleStrInt(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tuple_str_int('1, 2, 3'), (1, 2, 3))

    def test_empty_string(self):
        self.assertEqual(tuple_str_int(''), ())

    def test_single_number(self):
        self.assertEqual(tuple_str_int('4'), (4,))

    def test_negative_numbers(self):
        self.assertEqual(tuple_str_int('-1, -2, -3'), (-1, -2, -3))

    def test_zero(self):
        self.assertEqual(tuple_str_int('0'), (0,))

    def test_large_numbers(self):
        self.assertEqual(tuple_str_int('1000000, 2000000, 3000000'), (1000000, 2000000, 3000000))

    def test_with_parentheses(self):
        self.assertEqual(tuple_str_int('(1, 2, 3)'), (1, 2, 3))

    def test_with_ellipsis(self):
        self.assertEqual(tuple_str_int('1...2...3'), (1, 2, 3))

    def test_with_extra_spaces(self):
        self.assertEqual(tuple_str_int(' 1 , 2 , 3 '), (1, 2, 3))

    def test_with_mixed_spaces_and_parentheses(self):
        self.assertEqual(tuple_str_int('(1, 2, 3)'), (1, 2, 3))
