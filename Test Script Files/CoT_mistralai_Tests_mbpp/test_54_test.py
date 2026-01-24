import unittest
from mbpp_54_code import counting_sort

class TestCountingSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(counting_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(counting_sort([1]), [1])

    def test_sorted_list(self):
        self.assertEqual(counting_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(counting_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(counting_sort([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), [1, 1, 2, 2, 3, 3, 4, 4, 5, 5])

    def test_large_positive_numbers(self):
        self.assertEqual(counting_sort([100000, 99999, 99998, 1, 2, 3]), [1, 2, 3, 99998, 99999, 100000])

    def test_negative_numbers(self):
        self.assertEqual(counting_sort([-1, -2, -3, 1, 2, 3]), [-3, -2, -1, 1, 2, 3])

    def test_mixed_positive_and_negative_numbers(self):
        self.assertEqual(counting_sort([-1, -2, -3, 1, 2, 3]), [-3, -2, -1, 1, 2, 3])

    def test_invalid_input_type_list(self):
        with self.assertRaises(TypeError):
            counting_sort(123)

    def test_invalid_input_type_integer(self):
        with self.assertRaises(TypeError):
            counting_sort([1, 2, 3, "a"])
