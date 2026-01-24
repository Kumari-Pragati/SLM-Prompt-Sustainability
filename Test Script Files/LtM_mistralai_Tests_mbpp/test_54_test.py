import unittest
from mbpp_54_code import counting_sort

class TestCountingSort(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(counting_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_input(self):
        self.assertEqual(counting_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_single_element_input(self):
        self.assertEqual(counting_sort([7]), [7])

    def test_empty_input(self):
        self.assertEqual(counting_sort([]), [])

    def test_max_value_input(self):
        self.assertEqual(counting_sort(list(range(100))), list(range(100)))

    def test_min_value_input(self):
        self.assertEqual(counting_sort(list(range(-100, 0))), list(range(-100, 0)))

    def test_negative_and_positive_input(self):
        self.assertEqual(counting_sort(list(range(-5, 6))), list(range(-5, 6)))
