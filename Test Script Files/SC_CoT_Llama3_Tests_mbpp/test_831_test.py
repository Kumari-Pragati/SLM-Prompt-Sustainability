import unittest
from mbpp_831_code import count_Pairs

class TestCountPairs(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5], 5), 0)

    def test_pairs_present(self):
        self.assertEqual(count_Pairs([1, 2, 2, 3, 4, 5], 6), 1)

    def test_multiple_pairs(self):
        self.assertEqual(count_Pairs([1, 2, 2, 3, 3, 4, 5, 5], 8), 3)

    def test_no_pairs(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5, 6, 7, 8], 8), 0)

    def test_empty_array(self):
        self.assertEqual(count_Pairs([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(count_Pairs([1], 1), 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            count_Pairs("hello", 5)

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            count_Pairs([1, 2, 3], "hello")

    def test_invalid_input_type3(self):
        with self.assertRaises(TypeError):
            count_Pairs([1, 2, 3], [4, 5, 6])
