import unittest
from mbpp_476_code import big_sum

class TestBigSum(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(big_sum([1, 2, 3, 4, 5]), 10)

    def test_edge_case_empty_list(self):
        self.assertEqual(big_sum([]), 0)

    def test_boundary_case_single_element(self):
        self.assertEqual(big_sum([5]), 10)

    def test_complex_case_negative_numbers(self):
        self.assertEqual(big_sum([-1, -2, -3, -4, -5]), -10)

    def test_complex_case_mixed_numbers(self):
        self.assertEqual(big_sum([-1, 2, -3, 4, -5]), 6)
