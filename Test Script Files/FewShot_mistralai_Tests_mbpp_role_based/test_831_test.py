import unittest
from mbpp_831_code import count_Pairs

class TestCountPairs(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_Pairs([1, 2, 2, 3, 4, 4], 6), 2)

    def test_empty_list(self):
        self.assertEqual(count_Pairs([], 0), 0)

    def test_single_element(self):
        self.assertEqual(count_Pairs([1], 1), 0)

    def test_single_pair(self):
        self.assertEqual(count_Pairs([1, 1], 2), 1)

    def test_all_same(self):
        self.assertEqual(count_Pairs([1, 1, 1], 3), 2)

    def test_all_different(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4], 4), 0)

    def test_negative_numbers(self):
        self.assertEqual(count_Pairs([-1, -2, -2, -3], 4), 2)

    def test_invalid_input_arr(self):
        with self.assertRaises(TypeError):
            count_Pairs(1.5, 2)

    def test_invalid_input_n(self):
        with self.assertRaises(ValueError):
            count_Pairs([1, 2, 3], -1)
