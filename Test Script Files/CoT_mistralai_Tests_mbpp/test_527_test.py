import unittest
from mbpp_527_code import get_pairs_count

class TestGetPairsCount(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(get_pairs_count([], 0, 0), 0)

    def test_single_element_array(self):
        self.assertEqual(get_pairs_count([1], 1, 1), 0)
        self.assertEqual(get_pairs_count([1], 1, 2), 0)

    def test_pair_in_array(self):
        self.assertEqual(get_pairs_count([1, 2], 2, 3), 1)
        self.assertEqual(get_pairs_count([1, 2], 2, 4), 0)

    def test_multiple_pairs_in_array(self):
        self.assertEqual(get_pairs_count([1, 2, 3, 2], 4, 4), 2)

    def test_sum_greater_than_array_sum(self):
        self.assertEqual(get_pairs_count([1, 2], 2, 3), 0)

    def test_negative_numbers(self):
        self.assertEqual(get_pairs_count([-1, -2], 2, 1), 0)
        self.assertEqual(get_pairs_count([-1, -2], 2, 0), 1)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, get_pairs_count, [1, 2], 'n', 3)
        self.assertRaises(TypeError, get_pairs_count, [1, 2], n=1, sum=3.5)
