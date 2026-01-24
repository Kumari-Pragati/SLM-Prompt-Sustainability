import unittest
from mbpp_54_code import counting_sort

class TestCountingSort(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(counting_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(counting_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(counting_sort([-1, -2, -3, -4, -5]), [-5, -4, -3, -2, -1])

    def test_edge_case_empty_list(self):
        self.assertEqual(counting_sort([]), [])

    def test_edge_case_single_element(self):
        self.assertEqual(counting_sort([0]), [0])
        self.assertEqual(counting_sort([10]), [10])

    def test_edge_case_max_value(self):
        self.assertEqual(counting_sort([0, 1, 2, 999999]), [0, 1, 2, 999999])

    def test_corner_case_negative_numbers(self):
        self.assertEqual(counting_sort([-1, 0, 1]), [-1, 0, 1])
        self.assertEqual(counting_sort([-100, -50, 50, 100]), [-100, -50, 50, 100])
