import unittest
from mbpp_231_code import max_sum

class TestMaxSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_sum([[0, 3, 2], [5, 8, 4], [9, 2, 3]], 3), 15)
        self.assertEqual(max_sum([[3], [8, 5]], 2), 13)
        self.assertEqual(max_sum([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], 4), 8)

    def test_edge_case(self):
        self.assertEqual(max_sum([[0]], 1), 0)
        self.assertEqual(max_sum([[0, 0]], 2), 0)
        self.assertEqual(max_sum([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], 5), 15)

    def test_invalid_input(self):
        self.assertRaises(TypeError, max_sum, [1, 2, 3], 'invalid')
        self.assertRaises(TypeError, max_sum, [1, 2, 3], 0)
        self.assertRaises(TypeError, max_sum, [1, 2, 3], -1)
