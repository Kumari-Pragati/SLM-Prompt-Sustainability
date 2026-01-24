import unittest
from mbpp_588_code import big_diff

class TestBigDiff(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(big_diff([1, 2, 3]), 2)
        self.assertEqual(big_diff([-1, -2, -3]), 4)
        self.assertEqual(big_diff([0, 0, 0]), 0)

    def test_edge_and_boundary(self):
        self.assertEqual(big_diff([-9223372036854775808, -1, 0]), 9223372036854775807)
        self.assertEqual(big_diff([1, 2, 9223372036854775807]), 9223372036854775806)
        self.assertEqual(big_diff([-1, -2, -3, -4, -5]), 5)
        self.assertEqual(big_diff([9223372036854775807, 9223372036854775806, 9223372036854775805]), 1)

    def test_complex(self):
        self.assertEqual(big_diff([-1, 0, 1, 0, -1]), 2)
        self.assertEqual(big_diff([1000000000000000000, -1000000000000000000]), 2000000000000000000)
        self.assertEqual(big_diff([-1000000000000000000, -999999999999999999, -999999999999999998, -1]), 1999999999999999999)
