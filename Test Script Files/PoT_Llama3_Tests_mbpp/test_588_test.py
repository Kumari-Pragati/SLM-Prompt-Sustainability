import unittest
from mbpp_588_code import big_diff

class TestBigDiff(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(big_diff([1, 2, 3, 4, 5]), 4)

    def test_edge_case_min_max_close(self):
        self.assertEqual(big_diff([1, 2, 3, 2, 1]), 2)

    def test_edge_case_min_max_far(self):
        self.assertEqual(big_diff([1, 100, 2, 3, 4]), 99)

    def test_edge_case_min_max_equal(self):
        self.assertEqual(big_diff([1, 1, 1, 1, 1]), 0)

    def test_edge_case_empty_list(self):
        with self.assertRaises(IndexError):
            big_diff([])

    def test_edge_case_single_element_list(self):
        with self.assertRaises(IndexError):
            big_diff([1])

    def test_edge_case_two_element_list(self):
        with self.assertRaises(IndexError):
            big_diff([1, 2])
