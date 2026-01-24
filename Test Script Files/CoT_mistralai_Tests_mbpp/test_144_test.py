import unittest
from mbpp_144_code import sum_Pairs

class TestSumPairs(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_Pairs([], 0), 0)

    def test_single_element(self):
        self.assertEqual(sum_Pairs([1], 1), 0)

    def test_simple_pair(self):
        self.assertEqual(sum_Pairs([1, 2], 2), 0)

    def test_multiple_pairs(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4], 4), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_Pairs([-1, -2, -3], 3), 15)

    def test_zero(self):
        self.assertEqual(sum_Pairs([0, 0, 0], 3), 0)

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            sum_Pairs([1, 2, 3], 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            sum_Pairs('abc', 3)
