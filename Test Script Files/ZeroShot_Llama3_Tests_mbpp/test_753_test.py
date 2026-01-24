import unittest
from mbpp_753_code import min_k

class TestMinK(unittest.TestCase):

    def test_min_k(self):
        self.assertEqual(min_k([[5, 10], [10, 20], [15, 30], [20, 40]], 2), [[5, 10], [10, 20]])
        self.assertEqual(min_k([[5, 10], [10, 20], [15, 30], [20, 40]], 3), [[5, 10], [10, 20], [15, 30]])
        self.assertEqual(min_k([[5, 10], [10, 20], [15, 30], [20, 40]], 1), [[5, 10]])
        self.assertEqual(min_k([[5, 10], [10, 20], [15, 30], [20, 40]], 4), [[5, 10], [10, 20], [15, 30], [20, 40]])
        self.assertEqual(min_k([[5, 10], [10, 20], [15, 30], [20, 40]], 0), [])
