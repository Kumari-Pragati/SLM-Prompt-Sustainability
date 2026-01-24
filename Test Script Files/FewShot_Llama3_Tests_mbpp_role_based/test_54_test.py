import unittest
from mbpp_54_code import counting_sort

class TestCountingSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(counting_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(counting_sort([5]), [5])

    def test_multiple_elements_list(self):
        self.assertEqual(counting_sort([2, 4, 1, 3, 5]), [1, 2, 3, 4, 5])

    def test_list_with_duplicates(self):
        self.assertEqual(counting_sort([2, 2, 1, 3, 3, 5]), [1, 2, 2, 3, 3, 5])

    def test_list_with_zero(self):
        self.assertEqual(counting_sort([0, 2, 4, 1, 3, 5]), [0, 1, 2, 3, 4, 5])

    def test_list_with_negative_numbers(self):
        self.assertEqual(counting_sort([-1, -2, 0, 1, 2, 3]), [-2, -1, 0, 1, 2, 3])

    def test_list_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            counting_sort([2, 4, 'a', 1, 3, 5])
