import unittest
from mbpp_10_code import small_nnum

class TestSmallNNum(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(small_nnum([1, 2, 3, 4, 5], 3), [1, 2, 3])
        self.assertEqual(small_nnum([10, 20, 30, 40, 50], 3), [10, 20, 30])

    def test_edge_cases(self):
        self.assertEqual(small_nnum([1], 1), [1])
        self.assertEqual(small_nnum([1, 2], 2), [1, 2])
        self.assertEqual(small_nnum([1, 2, 3], 1), [1])
        self.assertEqual(small_nnum([1, 2, 3], 4), [1, 2, 3])

    def test_boundary_cases(self):
        self.assertEqual(small_nnum([-1, -2, -3], 1), [-3])
        self.assertEqual(small_nnum([0, 0, 0], 1), [0])
        self.assertEqual(small_nnum([1, 2, 3], 0), [])

    def test_invalid_input_length(self):
        self.assertRaises(ValueError, small_nnum, [], 1)
        self.assertRaises(ValueError, small_nnum, [1], 0)
        self.assertRaises(ValueError, small_nnum, [1], -1)
        self.assertRaises(ValueError, small_nnum, [1, 2], 0)
        self.assertRaises(ValueError, small_nnum, [1, 2], len(list(range(-100, 100))) + 1)
