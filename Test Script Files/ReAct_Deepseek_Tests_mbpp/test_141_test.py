import unittest
from mbpp_141_code import pancake_sort

class TestPancakeSort(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(pancake_sort([3, 2, 1, 4]), [1, 2, 3, 4])
        self.assertEqual(pancake_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(pancake_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_edge_cases(self):
        self.assertEqual(pancake_sort([1]), [1])
        self.assertEqual(pancake_sort([]), [])

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            pancake_sort(123)
        with self.assertRaises(TypeError):
            pancake_sort('123')
        with self.assertRaises(TypeError):
            pancake_sort([1, '2', 3])
