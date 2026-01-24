import unittest
from mbpp_141_code import pancake_sort

class TestPancakeSort(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(pancake_sort([2, 1, 4, 3]), [1, 2, 3, 4])
        self.assertEqual(pancake_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(pancake_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_edge_conditions(self):
        self.assertEqual(pancake_sort([1]), [1])
        self.assertEqual(pancake_sort([]), [])

    def test_complex_cases(self):
        self.assertEqual(pancake_sort([5, 3, 2, 4, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(pancake_sort([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])
        self.assertEqual(pancake_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
