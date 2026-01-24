import unittest
from mbpp_819_code import count_duplic

class TestCountDuplic(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_duplic([]), ([], []))

    def test_single_element_list(self):
        self.assertEqual(count_duplic([1]), ([1], [1]))

    def test_duplicates_in_middle(self):
        self.assertEqual(count_duplic([1, 2, 1, 3, 2, 2]), ([1, 2, 1], [1, 1, 1, 2, 2, 2]))

    def test_duplicates_at_beginning(self):
        self.assertEqual(count_duplic([1, 1, 2]), ([1], [2, 1]))

    def test_duplicates_at_end(self):
        self.assertEqual(count_duplic([1, 2, 2]), ([1, 2], [1]))

    def test_only_duplicates(self):
        self.assertEqual(count_duplic([1, 1, 1]), ([1], [3]))

    def test_invalid_input_type_list(self):
        self.assertRaises(TypeError, count_duplic, "not a list")

    def test_invalid_input_type_element(self):
        self.assertRaises(TypeError, count_duplic, [1, "not a number"])
