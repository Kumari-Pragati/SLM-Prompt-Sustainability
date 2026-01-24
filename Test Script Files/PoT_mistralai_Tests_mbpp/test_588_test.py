import unittest
from mbpp_588_code import big_diff

class TestBigDiff(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(big_diff([1, 2, 3, 4, 5]), 4)

    def test_edge_case_single_element(self):
        self.assertEqual(big_diff([1]), 0)

    def test_edge_case_two_elements(self):
        self.assertEqual(big_diff([1, 2]), 1)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(big_diff([-1, -2]), 3)

    def test_corner_case_empty_list(self):
        self.assertEqual(big_diff([]), 0)
