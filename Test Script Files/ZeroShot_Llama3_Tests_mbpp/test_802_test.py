import unittest
from mbpp_802_code import count_Rotation

class TestCountRotation(unittest.TestCase):

    def test_count_rotation(self):
        self.assertEqual(count_Rotation([4, 3, 2, 1], 4), 1)
        self.assertEqual(count_Rotation([1, 2, 3, 4], 4), 0)
        self.assertEqual(count_Rotation([5, 6, 7, 8], 4), 0)
        self.assertEqual(count_Rotation([1, 2, 3, 4, 5], 5), 0)
        self.assertEqual(count_Rotation([5, 4, 3, 2, 1], 5), 1)
        self.assertEqual(count_Rotation([1, 2, 3, 4, 5, 6], 6), 0)
        self.assertEqual(count_Rotation([6, 5, 4, 3, 2, 1], 6), 1)
        self.assertEqual(count_Rotation([1, 2, 3, 4, 5, 6, 7], 7), 0)
        self.assertEqual(count_Rotation([7, 6, 5, 4, 3, 2, 1], 7), 1)
        self.assertEqual(count_Rotation([1, 2, 3, 4, 5, 6, 7, 8], 8), 0)
        self.assertEqual(count_Rotation([8, 7, 6, 5, 4, 3, 2, 1], 8), 1)
