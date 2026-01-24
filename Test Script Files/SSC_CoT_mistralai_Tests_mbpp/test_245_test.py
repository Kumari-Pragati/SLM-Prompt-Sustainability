import unittest
from mbpp_245_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 15)
        self.assertEqual(max_sum([-1, -2, -3, -4, -5], 5), 5)
        self.assertEqual(max_sum([0, 0, 0, 0, 0], 5), 0)

    def test_edge_cases(self):
        self.assertEqual(max_sum([1], 1), 1)
        self.assertEqual(max_sum([1, 2], 2), 3)
        self.assertEqual(max_sum([1, 2, 3], 3), 6)
        self.assertEqual(max_sum([1, 2, 3, 4], 4), 10)
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 1), 6)
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 6), 15)

    def test_boundary_cases(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 0), 0)
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 6), 15)
        self.assertEqual(max_sum([], 0), 0)
        self.assertEqual(max_sum([1], 0), 1)
        self.assertEqual(max_sum([1, 2], 0), 2)
        self.assertEqual(max_sum([1, 2, 3], 0), 3)
        self.assertEqual(max_sum([1, 2, 3, 4], 0), 4)
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 0), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_sum([-1, -2, -3, -4, -5], 5), -5)
        self.assertEqual(max_sum([-1, -2, -3, -4, -5], 1), -4)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, max_sum, [1, 2, 3], 'a')
        self.assertRaises(TypeError, max_sum, [1, 2, 3], (1, 2, 3))
        self.assertRaises(TypeError, max_sum, [1, 2, 3], {1: 2, 2: 3})
        self.assertRaises(ValueError, max_sum, [], 0)
        self.assertRaises(ValueError, max_sum, [1], 0)
        self.assertRaises(ValueError, max_sum, [1, 2], -1)
        self.assertRaises(ValueError, max_sum, [1, 2, 3], -6)
