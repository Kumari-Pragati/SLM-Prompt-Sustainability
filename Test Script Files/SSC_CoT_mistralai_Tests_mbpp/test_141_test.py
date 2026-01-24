import unittest
from mbpp_141_code import pancake_sort

class TestPancakeSort(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(pancake_sort([3, 2, 4, 1]), [1, 3, 2, 4])
        self.assertEqual(pancake_sort([1, 5, 3, 4, 2]), [1, 4, 5, 3, 2])
        self.assertEqual(pancake_sort([6, 5, 4, 7, 3, 2, 1]), [1, 7, 6, 5, 4, 3, 2])

    def test_edge_cases(self):
        self.assertEqual(pancake_sort([1]), [1])
        self.assertEqual(pancake_sort([2]), [2])
        self.assertEqual(pancake_sort([3]), [3])
        self.assertEqual(pancake_sort([4]), [4])
        self.assertEqual(pancake_sort([5]), [5])

    def test_boundary_cases(self):
        self.assertEqual(pancake_sort([0]), [0])
        self.assertEqual(pancake_sort([-1]), [1])
        self.assertEqual(pancake_sort([-2]), [1, -2])
        self.assertEqual(pancake_sort([-3]), [1, -3])
        self.assertEqual(pancake_sort([-4]), [1, -4])
        self.assertEqual(pancake_sort([-5]), [1, -5])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            pancake_sort(1.23)
        with self.assertRaises(TypeError):
            pancake_sort(True)
        with self.assertRaises(TypeError):
            pancake_sort(None)
