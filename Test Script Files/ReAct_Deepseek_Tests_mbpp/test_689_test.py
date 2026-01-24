import unittest
from mbpp_689_code import min_jumps

class TestMinJumps(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
        n = len(arr)
        self.assertEqual(min_jumps(arr, n), 3)

    def test_single_element(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(min_jumps(arr, n), 0)

    def test_zero_element(self):
        arr = []
        n = len(arr)
        self.assertEqual(min_jumps(arr, n), float('inf'))

    def test_zero_in_array(self):
        arr = [1, 3, 0, 8, 2, 0, 7]
        n = len(arr)
        self.assertEqual(min_jumps(arr, n), float('inf'))

    def test_max_jumps(self):
        arr = [10, 1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(min_jumps(arr, n), 1)

    def test_negative_numbers(self):
        arr = [-1, -3, -5, -8, -9, -2, -6, -7, -6, -8, -9]
        n = len(arr)
        self.assertEqual(min_jumps(arr, n), float('inf'))
