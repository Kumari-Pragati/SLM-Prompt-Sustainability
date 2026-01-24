import unittest
from mbpp_802_code import count_Rotation

class TestCountRotation(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Rotation([15, 18, 2, 3, 6, 12], 6), 2)
        self.assertEqual(count_Rotation([7, 9, 11, 12, 5], 5), 4)

    def test_edge_cases(self):
        self.assertEqual(count_Rotation([1], 1), 0)
        self.assertEqual(count_Rotation([], 0), 0)

    def test_boundary_cases(self):
        self.assertEqual(count_Rotation([2, 1], 2), 1)
        self.assertEqual(count_Rotation([2, 3, 1], 3), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Rotation("1,2,3", 3)
        with self.assertRaises(TypeError):
            count_Rotation([1, 2, 3], "3")
        with self.assertRaises(TypeError):
            count_Rotation([1, 2, 3], -1)
        with self.assertRaises(TypeError):
            count_Rotation([1, 2, 3], 4)
