import unittest
from mbpp_881_code import sum_even_odd

class TestSumEvenOdd(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(sum_even_odd([2, 4, 6, 8, 10]), 12)

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_even_odd([]), -1)

    def test_edge_case_single_element(self):
        self.assertEqual(sum_even_odd([5]), -1)

    def test_edge_case_single_even(self):
        self.assertEqual(sum_even_odd([2]), 2)

    def test_edge_case_single_odd(self):
        self.assertEqual(sum_even_odd([5]), -1)

    def test_edge_case_multiple_even(self):
        self.assertEqual(sum_even_odd([2, 4, 6, 8]), 20)

    def test_edge_case_multiple_odd(self):
        self.assertEqual(sum_even_odd([1, 3, 5, 7]), -1)

    def test_edge_case_mixed(self):
        self.assertEqual(sum_even_odd([2, 4, 5, 7]), 7)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            sum_even_odd("invalid_input")
