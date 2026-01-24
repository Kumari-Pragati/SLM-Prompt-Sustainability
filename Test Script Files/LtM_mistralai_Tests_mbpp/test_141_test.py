import unittest
from mbpp_141_code import pancake_sort

class TestPancakeSort(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(pancake_sort([3, 2, 4, 1]), [1, 3, 2, 4])
        self.assertEqual(pancake_sort([1]), [1])
        self.assertEqual(pancake_sort([4, 3, 2, 1]), [1, 3, 4, 2])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(pancake_sort([]), [])
        self.assertEqual(pancake_sort([1000000000]), [1000000000])
        self.assertEqual(pancake_sort([1] * 1000000000), [1] * 1000000000[::-1])

    def test_complex_scenarios(self):
        self.assertEqual(pancake_sort([1, 2, 2, 1]), [1, 2, 1, 2])
        self.assertEqual(pancake_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(pancake_sort([1, 1, 1]), [1, 1, 1])
