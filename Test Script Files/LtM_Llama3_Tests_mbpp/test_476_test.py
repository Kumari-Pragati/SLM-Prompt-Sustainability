import unittest
from mbpp_476_code import big_sum

class TestBigSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(big_sum([1, 2, 3]), 3)
        self.assertEqual(big_sum([-1, 0, 1]), 0)
        self.assertEqual(big_sum([5, 5, 5]), 5)

    def test_edge(self):
        self.assertEqual(big_sum([]), None)
        self.assertEqual(big_sum([1]), 1)
        self.assertEqual(big_sum([-1]), -1)

    def test_max_min(self):
        self.assertEqual(big_sum([10, 2]), 12)
        self.assertEqual(big_sum([-10, -2]), -2)
        self.assertEqual(big_sum([5, 5]), 5)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            big_sum('abc')
