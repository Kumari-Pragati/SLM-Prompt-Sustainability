import unittest
from mbpp_476_code import big_sum

class TestBigSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(big_sum([1, 2, 3]), 1 + 2)
        self.assertEqual(big_sum([-1, -2, -3]), -1 + (-2))
        self.assertEqual(big_sum([0, 0, 0]), 0)

    def test_edge_cases(self):
        self.assertEqual(big_sum([1000000000, -1000000000]), 1000000000 + (-1000000000))
        self.assertEqual(big_sum([-1000000000, 1000000000]), 1000000000 + (-1000000000))
        self.assertEqual(big_sum([1, 2, 3, 4, 5]), 1 + 2)
        self.assertEqual(big_sum([5, 4, 3, 2, 1]), 1 + 2)
        self.assertEqual(big_sum([-1, -2, -3, -4, -5]), -1 + (-2))
        self.assertEqual(big_sum([-5, -4, -3, -2, -1]), -1 + (-2))

    def test_empty_list(self):
        self.assertEqual(big_sum([]), None)
