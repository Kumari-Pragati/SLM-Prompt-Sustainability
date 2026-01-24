import unittest
from mbpp_54_code import counting_sort

class TestCountingSort(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(counting_sort([1, 3, 5, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(counting_sort([-1, -3, -5, -2, -4]), [-4, -3, -2, -1, -1])

    def test_edge_cases(self):
        self.assertEqual(counting_sort([0]), [0])
        self.assertEqual(counting_sort([1000000]), [0, 1, 2, ..., 999999, 1000000])
        self.assertEqual(counting_sort([1000000, 1]), [1, 0, 1, ..., 999998, 999999, 1000000])

    def test_boundary_conditions(self):
        self.assertEqual(counting_sort([]), [])
        self.assertEqual(counting_sort([1]), [0])
        self.assertEqual(counting_sort([1, 1]), [0, 0])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            counting_sort('abc')
        with self.assertRaises(TypeError):
            counting_sort(1.23)
