import unittest
from mbpp_270_code import sum_even_and_even_index

class TestSumEvenAndEvenIndex(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8], 8), 12)
        self.assertEqual(sum_even_and_even_index([-1, 0, 1, 2, 3, 4, 5, 6], 8), 0)
        self.assertEqual(sum_even_and_even_index([0, 0, 0, 0, 0, 0, 0, 0], 8), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5], 5), 2)
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5], 6), 2)
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5], 0), 0)
        self.assertEqual(sum_even_and_even_index([], 0), 0)
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5], 1), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_even_and_even_index([-1, -2, -3, -4, -5], 5), -6)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, sum_even_and_even_index, 'string', 5)
        self.assertRaises(TypeError, sum_even_and_even_index, [1, 2, 3], -1)
        self.assertRaises(TypeError, sum_even_and_even_index, [1, 2, 3], float('inf'))
