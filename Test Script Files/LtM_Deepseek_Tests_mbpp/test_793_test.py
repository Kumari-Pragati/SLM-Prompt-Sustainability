import unittest
from mbpp_793_code import last

class TestLast(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(last([1, 2, 3, 4, 5], 3, 5), 2)

    def test_edge_case_not_found(self):
        self.assertEqual(last([1, 2, 3, 4, 5], 6, 5), -1)

    def test_edge_case_empty_array(self):
        self.assertEqual(last([], 1, 0), -1)

    def test_boundary_case_single_element(self):
        self.assertEqual(last([5], 5, 1), 0)

    def test_complex_case_duplicates(self):
        self.assertEqual(last([1, 2, 3, 3, 4, 5], 3, 6), 3)

    def test_complex_case_multiple_duplicates(self):
        self.assertEqual(last([1, 2, 3, 3, 4, 4, 5], 4, 7), 5)
