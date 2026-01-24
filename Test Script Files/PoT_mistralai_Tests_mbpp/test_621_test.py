import unittest
from mbpp_621_code import increment_numerics

class TestIncrementNumerics(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(increment_numerics([1, 2, 'three', 4, 'five'], 2), ['3', '4', 'three', '6', 'five'])

    def test_edge_case_empty_list(self):
        self.assertEqual(increment_numerics([]), [])

    def test_edge_case_single_digit(self):
        self.assertEqual(increment_numerics([1]), ['2'])

    def test_edge_case_single_non_digit(self):
        self.assertEqual(increment_numerics(['a']), ['a'])

    def test_edge_case_single_string_with_digits(self):
        self.assertEqual(increment_numerics(['1a']), ['1a'])

    def test_edge_case_all_digits(self):
        self.assertEqual(increment_numerics([1, 2, 3]), ['2', '3', '4'])

    def test_corner_case_negative_numbers(self):
        self.assertEqual(increment_numerics([-1, -2], 3), ['2', '-1'])
