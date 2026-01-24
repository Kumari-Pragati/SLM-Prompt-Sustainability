import unittest
from mbpp_807_code import first_odd

class TestFirstOdd(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(first_odd([1, 2, 3, 4, 5]), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(first_odd([]), -1)

    def test_edge_case_single_element(self):
        self.assertEqual(first_odd([2]), -1)

    def test_edge_case_single_odd(self):
        self.assertEqual(first_odd([1]), 1)

    def test_edge_case_multiple_odd(self):
        self.assertEqual(first_odd([1, 3, 5, 7]), 1)

    def test_edge_case_multiple_even(self):
        self.assertEqual(first_odd([2, 4, 6, 8]), -1)

    def test_edge_case_mixed(self):
        self.assertEqual(first_odd([1, 2, 3, 4, 5, 6]), 1)
