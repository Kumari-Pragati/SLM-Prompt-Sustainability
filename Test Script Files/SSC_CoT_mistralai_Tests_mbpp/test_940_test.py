import unittest
from mbpp_940_code import shift_down

class TestShiftDown(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(shift_down([3, 5, 1, 7, 2, 9, 8, 4], 0, 7), [3, 1, 5, 7, 9, 8, 2, 4])
        self.assertEqual(shift_down([1, 3, 5, 7, 9, 8, 2, 4], 3, 6), [1, 3, 5, 7, 8, 9, 2, 4])
        self.assertEqual(shift_down([10, 9, 8, 7, 6, 5, 4, 3], 4, 7), [10, 9, 8, 7, 5, 6, 4, 3])

    def test_edge_cases(self):
        self.assertEqual(shift_down([], 0, -1), [])
        self.assertEqual(shift_down([1], 0, 0), [1])
        self.assertEqual(shift_down([1, 2], 0, 1), [2, 1])
        self.assertEqual(shift_down([1, 2], 1, 0), [1])
        self.assertEqual(shift_down([1, 2], 1, 1), [2])

    def test_boundary_cases(self):
        self.assertEqual(shift_down([1, 2], 0, 0), [1])
        self.assertEqual(shift_down([1, 2], 0, 1), [2, 1])
        self.assertEqual(shift_down([1, 2], 1, 1), [2])
        self.assertEqual(shift_down([1, 2], 0, 2), [2, 1])
        self.assertEqual(shift_down([1, 2], 1, 2), [1])

    def test_invalid_input(self):
        with self.assertRaises(IndexError):
            shift_down([1, 2], -1, 1)
        with self.assertRaises(IndexError):
            shift_down([1, 2], 1, -1)
