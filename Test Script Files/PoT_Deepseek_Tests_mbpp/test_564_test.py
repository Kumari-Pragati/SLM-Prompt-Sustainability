import unittest
from mbpp_564_code import count_Pairs

class TestCountPairs(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Pairs([1, 2, 3, 2, 1], 5), 2)

    def test_empty_array(self):
        self.assertEqual(count_Pairs([], 0), 0)

    def test_single_element(self):
        self.assertEqual(count_Pairs([1], 1), 0)

    def test_all_same_elements(self):
        self.assertEqual(count_Pairs([1, 1, 1, 1], 4), 0)

    def test_all_different_elements(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4], 4), 6)

    def test_large_array(self):
        self.assertEqual(count_Pairs(list(range(1, 1001)), 1000), 499500)

    def test_negative_numbers(self):
        self.assertEqual(count_Pairs([-1, -2, -3, -2, -1], 5), 2)

    def test_mixed_numbers(self):
        self.assertEqual(count_Pairs([-1, 0, 1, 0, -1], 5), 2)
