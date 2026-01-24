import unittest
from mbpp_218_code import min_Operations

class TestMinOperations(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Operations(10, 20), 1)

    def test_typical_case_2(self):
        self.assertEqual(min_Operations(3, 9), 1)

    def test_edge_case_A_greater_than_B(self):
        self.assertEqual(min_Operations(25, 15), 2)

    def test_edge_case_A_equals_B(self):
        self.assertEqual(min_Operations(10, 10), 0)

    def test_edge_case_B_is_zero(self):
        self.assertEqual(min_Operations(10, 0), 0)

    def test_edge_case_A_and_B_are_zero(self):
        self.assertEqual(min_Operations(0, 0), 0)

    def test_error_case_negative_numbers(self):
        with self.assertRaises(Exception):
            min_Operations(-10, 20)

    def test_error_case_non_integer_input(self):
        with self.assertRaises(Exception):
            min_Operations(10.5, 20)
