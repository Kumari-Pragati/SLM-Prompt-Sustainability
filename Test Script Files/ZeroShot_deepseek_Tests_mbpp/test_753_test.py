import unittest
from mbpp_753_code import min_k

class TestMinK(unittest.TestCase):

    def test_min_k(self):
        self.assertEqual(min_k([(1, 2), (3, 4), (5, 1)], 2), [(5, 1), (3, 4)])
        self.assertEqual(min_k([(1, 2), (3, 1), (5, 4)], 1), [(3, 1)])
        self.assertEqual(min_k([(1, 2), (3, 4), (5, 6)], 3), [(1, 2), (3, 4), (5, 6)])
        self.assertEqual(min_k([], 0), [])
        self.assertEqual(min_k([(1, 2), (3, 4), (5, 1)], 4), [(1, 2), (3, 4), (5, 1)])
