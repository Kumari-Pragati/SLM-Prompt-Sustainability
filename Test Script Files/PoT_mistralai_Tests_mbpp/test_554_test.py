import unittest
from mbpp_554_code import Split

class TestSplit(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(Split([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_edge_case_empty_list(self):
        self.assertListEqual(Split([]), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(Split([0]), [])

    def test_edge_case_all_even(self):
        self.assertListEqual(Split([2, 4, 6]), [])

    def test_edge_case_all_odd(self):
        self.assertListEqual(Split([1, 3, 5, 7]), [1, 3, 5, 7])
