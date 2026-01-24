import unittest
from mbpp_797_code import sum_in_Range

class TestSumInRange(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sum_in_Range(1, 3), 2)
        self.assertEqual(sum_in_Range(5, 7), 10)
        self.assertEqual(sum_in_Range(11, 13), 26)

    def test_edge_input(self):
        self.assertEqual(sum_in_Range(0, 1), 0)
        self.assertEqual(sum_in_Range(2, 3), 1)
        self.assertEqual(sum_in_Range(1000000000, 1000000001), 500000001)

    def test_boundary_input(self):
        self.assertEqual(sum_in_Range(-1, 1), 0)
        self.assertEqual(sum_in_Range(1, -1), 0)
        self.assertEqual(sum_in_Range(1, 0), 0)

    def test_negative_input(self):
        self.assertEqual(sum_in_Range(-1, -2), 1)
        self.assertEqual(sum_in_Range(-2, -3), 3)

    def test_large_input(self):
        self.assertEqual(sum_in_Range(1000000000, 2000000000), 1000000001)
