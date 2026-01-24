import unittest
from mbpp_802_code import count_Rotation

class TestCountRotation(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_Rotation([], 0), 0)

    def test_single_element(self):
        self.assertEqual(count_Rotation([1], 1), 0)

    def test_increasing_sequence(self):
        self.assertEqual(count_Rotation([1, 2, 3, 4], 4), 0)

    def test_decreasing_sequence(self):
        self.assertEqual(count_Rotation([4, 3, 2, 1], 4), 0)

    def test_rotated_sequence(self):
        self.assertEqual(count_Rotation([3, 4, 5, 1, 2], 5), 1)

    def test_rotated_sequence_with_duplicates(self):
        self.assertEqual(count_Rotation([3, 3, 4, 5, 1, 2], 6), 1)

    def test_rotated_sequence_with_zero(self):
        self.assertEqual(count_Rotation([0, 1, 2, 3, 4], 5), 4)

    def test_rotated_sequence_with_negative(self):
        self.assertEqual(count_Rotation([-1, -2, 0, 1, 2], 5), 4)

    def test_rotated_sequence_with_long_sequence(self):
        self.assertEqual(count_Rotation([100, 101, 102, 1, 2], 5), 4)

    def test_rotated_sequence_with_negative_numbers(self):
        self.assertEqual(count_Rotation([-1, -2, -3, -4, -5], 5), 4)

    def test_rotated_sequence_with_empty_space(self):
        self.assertEqual(count_Rotation([1, 2, 3, None, 4], 5), 4)

    def test_rotated_sequence_with_large_numbers(self):
        self.assertEqual(count_Rotation([1000000, 1000001, 1000002, 1, 2], 5), 4)

    def test_rotated_sequence_with_large_numbers_and_empty_space(self):
        self.assertEqual(count_Rotation([1000000, 1000001, 1000002, None, 4], 5), 4)

    def test_rotated_sequence_with_negative_numbers_and_empty_space(self):
        self.assertEqual(count_Rotation([-1000000, -1000001, -1000002, None, 4], 5), 4)
