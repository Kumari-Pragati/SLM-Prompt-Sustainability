import unittest
from mbpp_819_code import count_duplic

class TestCountDuplic(unittest.TestCase):

    def test_empty_list(self):
        result, frequency = count_duplic([])
        self.assertEqual(result, [])
        self.assertEqual(frequency, [0])

    def test_single_element_list(self):
        result, frequency = count_duplic([1])
        self.assertEqual(result, [1])
        self.assertEqual(frequency, [1])

    def test_duplicate_elements_list(self):
        result, frequency = count_duplic([1, 1, 2, 2, 3, 3])
        self.assertEqual(result, [1, 1, 2, 2, 3])
        self.assertEqual(frequency, [2, 2, 2])

    def test_list_with_one_duplicate(self):
        result, frequency = count_duplic([1, 1, 2, 3])
        self.assertEqual(result, [1, 2, 3])
        self.assertEqual(frequency, [1, 1])

    def test_list_with_multiple_duplicates(self):
        result, frequency = count_duplic([1, 1, 1, 2, 2, 2, 3, 3, 3])
        self.assertEqual(result, [1, 2, 3, 3])
        self.assertEqual(frequency, [3, 3, 3])

    def test_list_with_only_duplicates(self):
        result, frequency = count_duplic([1, 1, 1, 1])
        self.assertEqual(result, [1])
        self.assertEqual(frequency, [4])

    def test_list_with_no_duplicates(self):
        result, frequency = count_duplic([1, 2, 3, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])
        self.assertEqual(frequency, [1] * len(result))

    def test_list_with_negative_numbers(self):
        result, frequency = count_duplic([-1, -1, 0, 1, 1])
        self.assertEqual(result, [-1, 0, 1])
        self.assertEqual(frequency, [2, 1, 2])

    def test_list_with_mixed_types(self):
        with self.assertRaises(TypeError):
            count_duplic([1, "a", 2])
