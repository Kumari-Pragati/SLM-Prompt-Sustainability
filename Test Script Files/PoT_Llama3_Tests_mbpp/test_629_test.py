import unittest
from mbpp_629_code import Split

class TestSplit(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Split([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_edge_case_empty_list(self):
        self.assertEqual(Split([]), [])

    def test_edge_case_single_element(self):
        self.assertEqual(Split([1]), [])

    def test_edge_case_all_even(self):
        self.assertEqual(Split([2, 4, 6, 8, 10]), [2, 4, 6, 8, 10])

    def test_edge_case_all_odd(self):
        self.assertEqual(Split([1, 3, 5, 7, 9]), [])

    def test_edge_case_mixed(self):
        self.assertEqual(Split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [2, 4, 6, 8, 10])
