import unittest
from mbpp_802_code import count_Rotation

class TestCountRotation(unittest.TestCase):

    def test_count_Rotation_ascending(self):
        self.assertEqual(count_Rotation([1, 2, 3, 4, 5], 5), 0)

    def test_count_Rotation_descending(self):
        self.assertEqual(count_Rotation([5, 4, 3, 2, 1], 5), 4)

    def test_count_Rotation_single_element(self):
        self.assertEqual(count_Rotation([1], 1), 0)

    def test_count_Rotation_duplicates(self):
        self.assertEqual(count_Rotation([1, 2, 1, 2, 2], 5), 2)

    def test_count_Rotation_rotated(self):
        self.assertEqual(count_Rotation([3, 4, 5, 1, 2], 5), 3)
