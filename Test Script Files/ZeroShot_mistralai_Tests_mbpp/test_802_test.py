import unittest
from802_code import count_Rotation

class TestCountRotation(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_Rotation([], 0), 0)

    def test_single_element(self):
        self.assertEqual(count_Rotation([1], 1), 0)

    def test_rotated_list(self):
        self.assertEqual(count_Rotation([5, 6, 7, 1, 2], 5), 1)

    def test_not_rotated_list(self):
        self.assertEqual(count_Rotation([1, 2, 3, 4, 5], 5), 0)

    def test_negative_numbers(self):
        self.assertEqual(count_Rotation([-1, -2, -3, 0, 1], 5), 1)

    def test_duplicates(self):
        self.assertEqual(count_Rotation([1, 1, 2, 3], 4), 1)
