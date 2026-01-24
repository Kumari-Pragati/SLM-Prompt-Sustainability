import unittest
from mbpp_689_code import min_jumps

class TestMinJumps(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
        n = len(arr)
        self.assertEqual(min_jumps(arr, n), 3)

    def test_edge_case_single_element(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(min_jumps(arr, n), 0)

    def test_edge_case_zero_element(self):
        arr = []
        n = len(arr)
        self.assertEqual(min_jumps(arr, n), float('inf'))

    def test_edge_case_zero_in_array(self):
        arr = [1, 0, 3, 6, 3, 2, 3, 6, 8, 9]
        n = len(arr)
        self.assertEqual(min_jumps(arr, n), float('inf'))

    def test_corner_case_large_jumps(self):
        arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        n = len(arr)
        self.assertEqual(min_jumps(arr, n), 3)

    def test_invalid_input_negative_values(self):
        arr = [-1, -3, -6, -3, -2, -3, -6, -8, -9, -5]
        n = len(arr)
        with self.assertRaises(ValueError):
            min_jumps(arr, n)

    def test_invalid_input_non_integer_values(self):
        arr = [1, 3, 6, 3, 2, 3, 6, 8, 'nine', 5]
        n = len(arr)
        with self.assertRaises(TypeError):
            min_jumps(arr, n)
