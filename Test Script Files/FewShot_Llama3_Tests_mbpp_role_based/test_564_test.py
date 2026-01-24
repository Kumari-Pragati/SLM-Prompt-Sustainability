import unittest
from mbpp_564_code import count_Pairs

class TestCountPairs(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(count_Pairs([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(count_Pairs([1], 1), 0)

    def test_two_element_array(self):
        self.assertEqual(count_Pairs([1, 2], 2), 1)

    def test_three_element_array(self):
        self.assertEqual(count_Pairs([1, 2, 3], 3), 2)

    def test_duplicates_in_array(self):
        self.assertEqual(count_Pairs([1, 2, 2, 3], 4), 2)

    def test_large_array(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 45)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            count_Pairs("abc", 0)

    def test_invalid_input_value(self):
        with self.assertRaises(TypeError):
            count_Pairs([1, 2, 3], "abc")
