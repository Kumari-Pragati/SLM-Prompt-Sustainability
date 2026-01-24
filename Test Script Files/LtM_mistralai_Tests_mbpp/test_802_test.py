import unittest
from mbpp_802_code import count_Rotation

class TestCountRotation(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(count_Rotation([4, 5, 6, 7, 8], 5), 1)
        self.assertEqual(count_Rotation([1, 2, 3, 4, 5], 5), 0)

    def test_edge_case(self):
        self.assertEqual(count_Rotation([2, 1], 2), 1)
        self.assertEqual(count_Rotation([1, 2, 1], 3), 1)
        self.assertEqual(count_Rotation([1, 1, 1], 3), 0)

    def test_boundary_case(self):
        self.assertEqual(count_Rotation([], 0), 0)
        self.assertEqual(count_Rotation([1], 1), 0)

    def test_negative_case(self):
        self.assertEqual(count_Rotation([-1, -2, -3], 3), 0)

    def test_complex_case(self):
        self.assertEqual(count_Rotation([1, 2, 3, 5, 4], 5), 3)
        self.assertEqual(count_Rotation([8, 7, 6, 5, 4, 3, 2, 1], 8), 0)
