import unittest
from mbpp_959_code import Average

class TestAverage(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(Average([1, 2, 3, 4, 5]), 3)

    def test_edge_case_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            Average([])

    def test_edge_case_single_element_list(self):
        self.assertEqual(Average([1]), 1)

    def test_edge_case_zero_sum(self):
        self.assertEqual(Average([-1, 0, 1]), 0)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(Average([-1, -2, -3]), -2)

    def test_edge_case_positive_numbers(self):
        self.assertEqual(Average([1, 2, 3]), 2)

    def test_edge_case_mixed_numbers(self):
        self.assertEqual(Average([-1, 0, 1, 2, 3]), 1)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            Average("hello")
