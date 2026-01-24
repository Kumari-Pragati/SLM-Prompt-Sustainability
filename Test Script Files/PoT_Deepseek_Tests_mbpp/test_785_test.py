import unittest
from mbpp_785_code import tuple_str_int

class TestTupleStrInt(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tuple_str_int("1, 2, 3"), (1, 2, 3))

    def test_edge_case_single_number(self):
        self.assertEqual(tuple_str_int("4"), (4,))

    def test_boundary_case_empty_string(self):
        self.assertEqual(tuple_str_int(""), ())

    def test_boundary_case_large_numbers(self):
        self.assertEqual(tuple_str_int("1000000, 2000000, 3000000"), (1000000, 2000000, 3000000))

    def test_corner_case_negative_numbers(self):
        self.assertEqual(tuple_str_int("-1, -2, -3"), (-1, -2, -3))

    def test_corner_case_mixed_positive_negative(self):
        self.assertEqual(tuple_str_int("1, -1, 2, -2, 3, -3"), (1, -1, 2, -2, 3, -3))

    def test_corner_case_decimal_numbers(self):
        self.assertEqual(tuple_str_int("1.5, 2.5, 3.5"), (1, 2, 3))

    def test_corner_case_string_with_spaces(self):
        self.assertEqual(tuple_str_int("1, 2, 3, 4, 5"), (1, 2, 3, 4, 5))

    def test_corner_case_string_with_extra_spaces(self):
        self.assertEqual(tuple_str_int(" 1 ,  2 , 3 , 4 , 5 "), (1, 2, 3, 4, 5))

    def test_corner_case_string_with_extra_chars(self):
        self.assertEqual(tuple_str_int("1a, 2b, 3c"), (1, 2, 3))
