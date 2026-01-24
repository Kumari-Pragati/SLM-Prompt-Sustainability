import unittest
from mbpp_370_code import float_sort

class TestFloatSort(unittest.TestCase):
    def test_sort_positive_numbers(self):
        data = [(3.14, 3.14), (2.71, 2.71), (1.618, 1.618)]
        self.assertEqual(float_sort(data), [(3.14, 3.14), (2.71, 2.71), (1.618, 1.618)])

    def test_sort_negative_numbers(self):
        data = [(-3.14, -3.14), (-2.71, -2.71), (-1.618, -1.618)]
        self.assertEqual(float_sort(data), [(-3.14, -3.14), (-2.71, -2.71), (-1.618, -1.618)])

    def test_sort_mixed_numbers(self):
        data = [(3.14, 3.14), (-2.71, -2.71), (1.618, 1.618), (-0.01, -0.01), (0.0, 0.0)]
        self.assertEqual(float_sort(data), [(3.14, 3.14), (-2.71, -2.71), (1.618, 1.618), (-0.01, -0.01), (0.0, 0.0)])

    def test_sort_zero_and_negative(self):
        data = [(0.0, 0.0), (-0.0, -0.0)]
        self.assertEqual(float_sort(data), [(0.0, 0.0), (-0.0, -0.0)])

    def test_sort_zero_and_positive(self):
        data = [(0.0, 0.0), (1.0, 1.0)]
        self.assertEqual(float_sort(data), [(1.0, 1.0), (0.0, 0.0)])

    def test_sort_empty_list(self):
        self.assertEqual(float_sort([]), [])

    def test_sort_list_with_string(self):
        data = [('3.14', 3.14), ('2.71', 2.71), ('1.618', 1.618)]
        self.assertEqual(float_sort(data), [(3.14, 3.14), (2.71, 2.71), (1.618, 1.618)])

    def test_sort_list_with_integer(self):
        data = [(3, 3.0), (2, 2.0), (1, 1.0)]
        self.assertEqual(float_sort(data), [(3.0, 3), (2.0, 2), (1.0, 1)])
