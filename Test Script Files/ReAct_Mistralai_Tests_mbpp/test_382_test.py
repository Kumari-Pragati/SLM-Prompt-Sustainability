import unittest
from mbpp_382_code import find_rotation_code

class TestFindRotationCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_rotation_count([]), -1)

    def test_single_element(self):
        self.assertEqual(find_rotation_count([1]), 0)

    def test_rotated_list(self):
        self.assertEqual(find_rotation_count([3, 4, 5, 1]), 3)

    def test_rotated_list_with_duplicates(self):
        self.assertEqual(find_rotation_count([3, 4, 5, 1, 1]), 4)

    def test_rotated_list_with_multiple_rotations(self):
        self.assertEqual(find_rotation_count([8, 9, 1, 2, 3, 4, 5, 6, 7]), 6)

    def test_rotated_list_with_zero(self):
        self.assertEqual(find_rotation_count([0, 1, 2, 3, 4, 5, 6]), 7)

    def test_rotated_list_with_negative_numbers(self):
        self.assertEqual(find_rotation_count([-1, -2, 0, 1, 2]), 4)

    def test_rotated_list_with_large_numbers(self):
        self.assertEqual(find_rotation_count([1000000001, 1000000002, 1000000003, 1, 2]), 3)

    def test_list_in_reverse_order(self):
        self.assertEqual(find_rotation_count(list(reversed([1, 2, 3]))), 0)

    def test_list_with_duplicates_and_rotated(self):
        self.assertEqual(find_rotation_count([3, 3, 4, 1]), 2)

    def test_list_with_duplicates_and_rotated_multiple_times(self):
        self.assertEqual(find_rotation_count([3, 3, 3, 4, 1]), 3)

    def test_list_with_duplicates_and_rotated_multiple_times_at_end(self):
        self.assertEqual(find_rotation_count([1, 1, 1, 3, 3]), 4)

    def test_list_with_duplicates_and_rotated_multiple_times_at_beginning(self):
        self.assertEqual(find_rotation_count([3, 3, 1, 1]), 3)

    def test_list_with_duplicates_and_rotated_multiple_times_at_beginning_and_end(self):
        self.assertEqual(find_rotation_count([3, 3, 1, 1, 3]), 4)
