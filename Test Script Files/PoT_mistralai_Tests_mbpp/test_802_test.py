import unittest
from mbpp_802_code import count_Rotation

class TestCountRotation(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Rotation([1, 2, 3, 4, 5], 5), 1)
        self.assertEqual(count_Rotation([7, 6, 5, 4, 3, 2, 1], 7), 1)
        self.assertEqual(count_Rotation([1, 1, 1, 1, 1], 5), 0)

    def test_edge_cases(self):
        self.assertEqual(count_Rotation([1, 2, 3], 3), 1)
        self.assertEqual(count_Rotation([1, 2, 3], 4), 0)
        self.assertEqual(count_Rotation([1, 2, 3], 1), 0)

    def test_corner_cases(self):
        self.assertEqual(count_Rotation([1, 1, 1, 1, 1, 1], 7), 0)
        self.assertEqual(count_Rotation([-1, -2, -3], 3), 0)
        self.assertEqual(count_Rotation([1, 1, 1, 1, 1, 1, 1], 8), 1)
