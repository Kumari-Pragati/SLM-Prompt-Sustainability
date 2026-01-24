import unittest
from mbpp_802_code import count_Rotation

class TestCountRotation(unittest.TestCase):
    def test_positive_rotation(self):
        self.assertEqual(count_Rotation([1, 2, 3, 4], 4), 1)
        self.assertEqual(count_Rotation([4, 3, 2, 1], 4), 3)

    def test_zero_rotation(self):
        self.assertEqual(count_Rotation([1, 2, 3, 1], 4), 0)
        self.assertEqual(count_Rotation([1, 1, 1, 1], 4), 0)

    def test_negative_rotation(self):
        self.assertEqual(count_Rotation([3, 2, 1], 3), 0)
        self.assertEqual(count_Rotation([1, 3, 2], 3), 0)

    def test_empty_list(self):
        self.assertEqual(count_Rotation([], 0), 0)

    def test_single_element(self):
        self.assertEqual(count_Rotation([1], 1), 0)

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            count_Rotation([1, 2, 3], 0)
