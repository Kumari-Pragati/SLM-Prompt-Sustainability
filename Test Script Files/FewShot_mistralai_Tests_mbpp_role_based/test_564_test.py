import unittest
from mbpp_564_code import count_Pairs

class TestCountPairs(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(count_Pairs([1, 2, 2, 3, 4], 5), 3)

    def test_empty_list(self):
        self.assertEqual(count_Pairs([], 0), 0)

    def test_single_element(self):
        self.assertEqual(count_Pairs([1], 1), 0)

    def test_duplicate_first_and_last(self):
        self.assertEqual(count_Pairs([1, 1], 2), 1)

    def test_duplicate_elements(self):
        self.assertEqual(count_Pairs([1, 1, 2, 2, 3], 5), 3)

    def test_negative_numbers(self):
        self.assertEqual(count_Pairs([-1, -2, -2, -3, -4], 5), 3)

    def test_invalid_input_list(self):
        with self.assertRaises(TypeError):
            count_Pairs(1.5, 2)

    def test_invalid_input_n(self):
        with self.assertRaises(ValueError):
            count_Pairs([1, 2, 3], -1)
