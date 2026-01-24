import unittest
from mbpp_550_code import find_Max

class TestFindMax(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 4), 5)
        self.assertEqual(find_Max([10, 9, 8, 7, 6], 0, 4), 10)
        self.assertEqual(find_Max([-1, -2, -3, -4, -5], 0, 4), -1)

    def test_edge_input(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 0), 1)
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 4, 4), 5)
        self.assertEqual(find_Max([], 0, 0), None)
        self.assertEqual(find_Max([1], 0, 0), 1)

    def test_boundary_input(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 1), 2)
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 4, 3), 4)
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 1, 4), 5)
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 4), 5)

    def test_decreasing_array(self):
        self.assertEqual(find_Max([5, 4, 3, 2, 1], 0, 4), 5)

    def test_increasing_array(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 4), 5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Max('abc', 0, 0)
        with self.assertRaises(TypeError):
            find_Max([1, 2, 3], 3, -1)
        with self.assertRaises(TypeError):
            find_Max([1, 2, 3], -1, 0)
