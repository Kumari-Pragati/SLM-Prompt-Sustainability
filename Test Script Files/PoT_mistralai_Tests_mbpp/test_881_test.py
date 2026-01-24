import unittest
from mbpp_881_code import sum_even_odd

class TestSumEvenOdd(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_even_odd([1, 2, 3, 4, 5]), 3)
        self.assertEqual(sum_even_odd([2, 4, 6, 8]), 2)
        self.assertEqual(sum_even_odd([0, 1, 2, 3, 4]), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_even_odd([]), -1)

    def test_edge_case_single_element(self):
        self.assertEqual(sum_even_odd([1]), 1)
        self.assertEqual(sum_even_odd([2]), 2)

    def test_boundary_case_first_even_last_odd(self):
        self.assertEqual(sum_even_odd([2, 1]), 3)
        self.assertEqual(sum_even_odd([1, 2]), 3)

    def test_boundary_case_first_odd_last_even(self):
        self.assertEqual(sum_even_odd([1, 2]), 3)
        self.assertEqual(sum_even_odd([2, 1]), 3)
