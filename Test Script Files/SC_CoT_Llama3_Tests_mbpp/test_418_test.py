import unittest
from mbpp_418_code import Find_Max

class TestFind_Max(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(Find_Max([1, 2, 3, 4, 5]), 5)

    def test_edge_case_empty_list(self):
        self.assertIsNone(Find_Max([]))

    def test_edge_case_single_element_list(self):
        self.assertEqual(Find_Max([10]), 10)

    def test_edge_case_multiple_equal_max(self):
        self.assertEqual(Find_Max([1, 2, 2, 3, 4]), 4)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(Find_Max([-1, -2, -3, -4, -5]), -1)

    def test_edge_case_mixed_positive_negative(self):
        self.assertEqual(Find_Max([1, -2, 3, -4, 5]), 5)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            Find_Max("Invalid Input")

    def test_invalid_input_non_iterable(self):
        with self.assertRaises(TypeError):
            Find_Max(123)
