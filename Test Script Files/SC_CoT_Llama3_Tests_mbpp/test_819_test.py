import unittest
from mbpp_819_code import count_duplic

class TestCountDuplic(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_duplic([]), [])

    def test_single_element_list(self):
        self.assertEqual(count_duplic([1]), ([1], [1]))

    def test_no_duplicates(self):
        self.assertEqual(count_duplic([1, 2, 3, 4, 5]), ([1, 2, 3, 4, 5], [1, 1, 1, 1, 1]))

    def test_duplicates(self):
        self.assertEqual(count_duplic([1, 1, 2, 2, 3, 3, 4, 4, 5]), ([1, 1, 2, 2, 3, 3, 4, 4, 5], [2, 2, 3, 3, 4, 4, 1, 1, 5]))

    def test_duplicates_at_start(self):
        self.assertEqual(count_duplic([1, 1, 2, 3, 4, 5]), ([1, 1, 2, 3, 4, 5], [2, 1, 1, 1, 1, 1]))

    def test_duplicates_at_end(self):
        self.assertEqual(count_duplic([1, 2, 3, 4, 5, 5]), ([1, 2, 3, 4, 5, 5], [1, 1, 1, 1, 1, 1]))

    def test_duplicates_in_middle(self):
        self.assertEqual(count_duplic([1, 2, 2, 3, 3, 4, 5]), ([1, 2, 2, 3, 3, 4, 5], [1, 1, 2, 2, 2, 1, 1]))

    def test_duplicates_everywhere(self):
        self.assertEqual(count_duplic([1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5]), ([1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5], [3, 2, 1, 1, 1, 3, 2, 1, 1, 1, 1, 1, 1]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_duplic("abc")
