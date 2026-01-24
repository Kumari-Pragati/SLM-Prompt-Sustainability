import unittest
from mbpp_476_code import big_sum

class TestBigSum(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(big_sum([1, 2, 3, 4]), 1 + 4)
        self.assertEqual(big_sum([-1, -2, -3, -4]), -1 + -4)
        self.assertEqual(big_sum([0, 0, 0]), 0)

    def test_edge_cases(self):
        self.assertEqual(big_sum([1]), 1)
        self.assertEqual(big_sum([2, 3]), 2 + 3)
        self.assertEqual(big_sum([-1, -2]), -1 + -2)
        self.assertEqual(big_sum([-1, -2, -3]), -3 + -1)
        self.assertEqual(big_sum([float('inf'), float('-inf')]), float('inf') + float('-inf'))

    def test_empty_list(self):
        self.assertIsNone(big_sum([]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            big_sum('abc')
        with self.assertRaises(TypeError):
            big_sum(1.23)
        with self.assertRaises(TypeError):
            big_sum(True)
