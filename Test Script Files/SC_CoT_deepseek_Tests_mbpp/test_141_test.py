import unittest
from mbpp_141_code import pancake_sort

class TestPancakeSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(pancake_sort([3, 2, 1, 5, 4]), [1, 2, 3, 4, 5])

    def test_edge_case(self):
        self.assertEqual(pancake_sort([1]), [1])
        self.assertEqual(pancake_sort([]), [])

    def test_corner_case(self):
        self.assertEqual(pancake_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(pancake_sort([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            pancake_sort("1, 2, 3")
        with self.assertRaises(TypeError):
            pancake_sort(123)
