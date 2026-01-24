import unittest
from mbpp_831_code import count_Pairs

class TestCountPairs(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_Pairs([], 0), 0)

    def test_single_element(self):
        self.assertEqual(count_Pairs([1], 1), 0)

    def test_single_pair(self):
        self.assertEqual(count_Pairs([1, 1], 2), 1)

    def test_multiple_pairs(self):
        self.assertEqual(count_Pairs([1, 1, 2, 2, 3, 3], 6), 3)

    def test_no_pairs(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5], 5), 0)

    def test_duplicate_index(self):
        self.assertEqual(count_Pairs([1, 1, 2, 2, 2, 3], 6), 2)

    def test_negative_numbers(self):
        self.assertEqual(count_Pairs([-1, -1, 0, 1], 4), 1)

    def test_invalid_input_list(self):
        with self.assertRaises(TypeError):
            count_Pairs(1.5, 2)

    def test_invalid_input_n(self):
        with self.assertRaises(TypeError):
            count_Pairs([1, 2, 3], 'a')
