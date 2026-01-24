import unittest
from mbpp_476_code import big_sum

class TestBigSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(big_sum([1, 2, 3]), 4)

    def test_edge_case_min_max_equal(self):
        self.assertEqual(big_sum([-1, -1]), -2)

    def test_edge_case_min_max_negative(self):
        self.assertEqual(big_sum([-5, 5]), 0)

    def test_edge_case_min_max_positive(self):
        self.assertEqual(big_sum([5, 5]), 10)

    def test_edge_case_empty_list(self):
        with self.assertRaises(IndexError):
            big_sum([])

    def test_edge_case_single_element_list(self):
        self.assertEqual(big_sum([5]), 5)

    def test_edge_case_negative_list(self):
        self.assertEqual(big_sum([-1, -2, -3]), -6)

    def test_edge_case_positive_list(self):
        self.assertEqual(big_sum([1, 2, 3]), 6)
