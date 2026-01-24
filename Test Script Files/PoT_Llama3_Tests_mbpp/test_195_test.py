import unittest
from mbpp_195_code import first

class TestFirst(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(first([1, 2, 3, 4, 5], 3, 5), 2)

    def test_edge_case_lower(self):
        self.assertEqual(first([1, 2, 3, 4, 5], 1, 5), 0)

    def test_edge_case_higher(self):
        self.assertEqual(first([1, 2, 3, 4, 5], 5, 5), 4)

    def test_edge_case_equal(self):
        self.assertEqual(first([1, 2, 3, 4, 5], 3, 5), 2)

    def test_edge_case_empty(self):
        self.assertEqual(first([], 1, 0), -1)

    def test_edge_case_single(self):
        self.assertEqual(first([1], 1, 1), 0)

    def test_edge_case_zero(self):
        self.assertEqual(first([1, 2, 3, 4, 5], 1, 0), -1)
