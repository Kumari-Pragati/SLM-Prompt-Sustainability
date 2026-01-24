import unittest
from mbpp_54_code import counting_sort

class TestCountingSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(counting_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(counting_sort([1]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(counting_sort([1, 2, 3, 2, 1]), [1, 1, 2, 2, 3])

    def test_negative_numbers(self):
        self.assertEqual(counting_sort([-1, 0, 1]), [-1, 0, 1])

    def test_duplicates(self):
        self.assertEqual(counting_sort([1, 2, 2, 3, 3, 3]), [1, 2, 2, 3, 3, 3])

    def test_large_numbers(self):
        self.assertEqual(counting_sort([10, 20, 30, 40, 50]), [10, 20, 30, 40, 50])

    def test_non_integer_values(self):
        with self.assertRaises(TypeError):
            counting_sort([1, 2, 'a', 4])
