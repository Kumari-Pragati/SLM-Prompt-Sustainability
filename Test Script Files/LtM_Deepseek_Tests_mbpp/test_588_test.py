import unittest
from mbpp_588_code import big_diff

class TestBigDiff(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(big_diff([1, 2, 3]), 2)
        self.assertEqual(big_diff([1, 1, 1]), 0)
        self.assertEqual(big_diff([10, 2, 3]), 8)

    def test_edge_conditions(self):
        self.assertEqual(big_diff([1]), 0)
        self.assertEqual(big_diff([-1, -2]), 1)
        self.assertEqual(big_diff([100, 100]), 0)

    def test_boundary_conditions(self):
        self.assertEqual(big_diff([-1000000, 1000000]), 2000000)
        self.assertEqual(big_diff([-1, 0]), 1)
        self.assertEqual(big_diff([0, 1]), 1)

    def test_complex_cases(self):
        self.assertEqual(big_diff([1, 2, 3, 4, 5]), 4)
        self.assertEqual(big_diff([10, 9, 8, 7, 6]), 4)
        self.assertEqual(big_diff([-1, -2, -3, -4, -5]), 4)
