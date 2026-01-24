import unittest
from mbpp_802_code import count_Rotation

class TestCountRotation(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_Rotation([15, 18, 2, 3, 6, 12], 6), 2)

    def test_edge_condition(self):
        self.assertEqual(count_Rotation([1], 1), 0)

    def test_boundary_condition(self):
        self.assertEqual(count_Rotation([1, 2], 2), 1)
        self.assertEqual(count_Rotation([2, 1], 2), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Rotation("1, 2, 3", 3)
        with self.assertRaises(TypeError):
            count_Rotation([1, 2, 3], "3")
        with self.assertRaises(TypeError):
            count_Rotation([1, 2, 3], -1)
        with self.assertRaises(TypeError):
            count_Rotation([1, 2, 3], 0)
