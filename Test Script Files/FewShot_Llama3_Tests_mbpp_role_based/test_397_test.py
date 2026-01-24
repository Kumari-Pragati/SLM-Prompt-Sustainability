import unittest
from mbpp_397_code import median_numbers

class TestMedianNumbers(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(median_numbers(5, 3, 2), 3)

    def test_edge_case_a_greater_than_b_and_c(self):
        self.assertEqual(median_numbers(10, 5, 3), 10)

    def test_edge_case_b_greater_than_a_and_c(self):
        self.assertEqual(median_numbers(3, 10, 5), 5)

    def test_edge_case_c_greater_than_a_and_b(self):
        self.assertEqual(median_numbers(2, 3, 10), 10)

    def test_edge_case_a_equal_to_b_and_c(self):
        self.assertEqual(median_numbers(5, 5, 5), 5)

    def test_edge_case_b_equal_to_a_and_c(self):
        self.assertEqual(median_numbers(5, 5, 5), 5)

    def test_edge_case_c_equal_to_a_and_b(self):
        self.assertEqual(median_numbers(5, 5, 5), 5)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            median_numbers('a', 3, 2)
