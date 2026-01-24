import unittest
from mbpp_382_code import find_rotation_count

class TestFindRotationCount(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_rotation_count([]), -1)

    def test_single_element_list(self):
        self.assertEqual(find_rotation_count([1]), 0)

    def test_rotated_list(self):
        self.assertEqual(find_rotation_count([5, 6, 7, 1, 2, 3]), 1)

    def test_rotated_list_with_duplicates(self):
        self.assertEqual(find_rotation_count([3, 4, 5, 1, 2, 3]), 3)

    def test_rotated_list_with_multiple_rotations(self):
        self.assertEqual(find_rotation_count([7, 8, 9, 1, 2, 3, 4, 5, 6, 7]), 4)

    def test_list_in_reverse_order(self):
        self.assertEqual(find_rotation_count([3, 2, 1]), -1)

    def test_list_with_duplicates_and_rotation(self):
        self.assertEqual(find_rotation_count([1, 1, 2, 3]), 0)

    def test_list_with_multiple_duplicates_and_rotation(self):
        self.assertEqual(find_rotation_count([1, 1, 2, 1, 3]), 2)

    def test_list_with_negative_numbers(self):
        self.assertEqual(find_rotation_count([-1, -2, 0, 1, 2]), 0)

    def test_list_with_large_numbers(self):
        self.assertEqual(find_rotation_count([1000000001, 1000000002, 1000000003, 1, 2]), 3)
