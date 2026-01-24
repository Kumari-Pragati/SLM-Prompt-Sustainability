import unittest
from mbpp_476_code import big_sum

class TestBigSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(big_sum([1, 2, 3]), 4)

    def test_edge_case_min_negative(self):
        self.assertEqual(big_sum([-1, 2, 3]), -1)

    def test_edge_case_max_negative(self):
        self.assertEqual(big_sum([-1, -2, -3]), -1)

    def test_edge_case_min_zero(self):
        self.assertEqual(big_sum([0, 2, 3]), 2)

    def test_edge_case_max_zero(self):
        self.assertEqual(big_sum([0, 0, 0]), 0)

    def test_edge_case_min_positive(self):
        self.assertEqual(big_sum([1, 2, 3]), 4)

    def test_edge_case_max_positive(self):
        self.assertEqual(big_sum([1, 2, 3]), 4)

    def test_edge_case_all_negative(self):
        self.assertEqual(big_sum([-1, -2, -3]), -1)

    def test_edge_case_all_positive(self):
        self.assertEqual(big_sum([1, 2, 3]), 4)

    def test_edge_case_all_zero(self):
        self.assertEqual(big_sum([0, 0, 0]), 0)

    def test_edge_case_empty_list(self):
        with self.assertRaises(IndexError):
            big_sum([])
