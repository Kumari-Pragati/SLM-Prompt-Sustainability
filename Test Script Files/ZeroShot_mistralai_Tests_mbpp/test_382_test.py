import unittest
from mbpp_382_code import find_rotation_count

class TestFindRotationCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_rotation_count([]), -1)

    def test_single_element(self):
        self.assertEqual(find_rotation_count([1]), 0)

    def test_rotated_list_single_rotation(self):
        self.assertEqual(find_rotation_count([3, 4, 5, 1, 2]), 3)

    def test_rotated_list_multiple_rotations(self):
        self.assertEqual(find_rotation_count([6, 7, 8, 9, 10, 1, 2, 3]), 6)

    def test_unsorted_list(self):
        self.assertEqual(find_rotation_count([2, 6, 3, 1, 4]), 2)

    def test_list_with_duplicates(self):
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 1, 2, 3]), 4)

    def test_list_with_no_rotation(self):
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5]), 0)
