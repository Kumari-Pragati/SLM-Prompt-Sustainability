import unittest
from mbpp_476_code import big_sum

class TestBigSum(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(big_sum([1, 100]), 101)
        self.assertEqual(big_sum([-100, -1]), -99)
        self.assertEqual(big_sum([0, 0]), 0)

    def test_edge_cases(self):
        self.assertEqual(big_sum([1]), 1)
        self.assertEqual(big_sum([-1]), -1)
        self.assertEqual(big_sum([100]), 100)
        self.assertEqual(big_sum([-100]), -100)

    def test_empty_list(self):
        self.assertIsNone(big_sum([]))

    def test_single_zero(self):
        self.assertEqual(big_sum([0]), 0)

    def test_invalid_input(self):
        self.assertRaises(TypeError, big_sum, "not a list")
        self.assertRaises(TypeError, big_sum, [1, "two"])
