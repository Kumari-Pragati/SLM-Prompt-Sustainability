import unittest
from mbpp_126_code import sum

class TestSum(unittest.TestCase):

    def test_simple_sum(self):
        self.assertEqual(sum(4, 6), 2)
        self.assertEqual(sum(6, 4), 2)
        self.assertEqual(sum(8, 2), 2)
        self.assertEqual(sum(2, 8), 2)

    def test_edge_cases(self):
        self.assertEqual(sum(1, 1), 0)
        self.assertEqual(sum(0, 1), 0)
        self.assertEqual(sum(1, 0), 0)
        self.assertEqual(sum(0, 0), 0)

    def test_boundary_cases(self):
        self.assertEqual(sum(2147483647, 1), 1)
        self.assertEqual(sum(1, 2147483647), 1)
        self.assertEqual(sum(2147483647, 2147483647), 2147483646)

    def test_complex_cases(self):
        self.assertEqual(sum(12, 20), 4)
        self.assertEqual(sum(20, 12), 4)
        self.assertEqual(sum(12, 12), 0)
        self.assertEqual(sum(20, 20), 0)
