import unittest
from mbpp_71_code import comb_sort

class TestCombSort(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(comb_sort([5, 3, 1, 6, 4, 2]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(comb_sort([10, 20, 30, 40, 50]), [10, 20, 30, 40, 50])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(comb_sort([1]), [1])
        self.assertEqual(comb_sort([1, 1]), [1, 1])
        self.assertEqual(comb_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(comb_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_negative_numbers(self):
        self.assertEqual(comb_sort([-1, -2, -3]), [-3, -2, -1])
        self.assertEqual(comb_sort([-1, 0, -2]), [-1, 0, -2])
        self.assertEqual(comb_sort([-1, 1, -2, 2]), [-1, 1, -2, 2])

    def test_floats(self):
        self.assertEqual(comb_sort([1.1, 2.2, 3.3]), [1.1, 2.2, 3.3])
        self.assertEqual(comb_sort([3.3, 2.2, 1.1]), [1.1, 2.2, 3.3])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            comb_sort('abc')
        with self.assertRaises(TypeError):
            comb_sort([1, 2, 3, 'a'])
