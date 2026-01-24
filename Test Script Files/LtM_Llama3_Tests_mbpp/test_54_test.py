import unittest
from mbpp_54_code import counting_sort

class TestCountingSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(counting_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(counting_sort([1]), [1])

    def test_single_element_list_with_duplicates(self):
        self.assertEqual(counting_sort([1, 1]), [1, 1])

    def test_multiple_elements_list(self):
        self.assertEqual(counting_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_multiple_elements_list_with_duplicates(self):
        self.assertEqual(counting_sort([1, 2, 2, 3, 3, 3, 4, 5, 5]), [1, 2, 2, 3, 3, 3, 4, 5, 5])

    def test_max_value_at_end(self):
        self.assertEqual(counting_sort([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_max_value_at_start(self):
        self.assertEqual(counting_sort([6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6])

    def test_max_value_at_middle(self):
        self.assertEqual(counting_sort([3, 2, 1, 4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_max_value_at_middle_with_duplicates(self):
        self.assertEqual(counting_sort([3, 2, 2, 1, 4, 4, 5, 5, 6]), [1, 2, 2, 3, 4, 4, 5, 5, 6])
