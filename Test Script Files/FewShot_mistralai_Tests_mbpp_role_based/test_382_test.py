import unittest
from mbpp_382_code import find_rotation_count

class TestFindRotationCount(unittest.TestCase):
    def test_rotated_array(self):
        self.assertEqual(find_rotation_count([4, 5, 6, 7, 0, 1, 2]), 4)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7]), -1)
        self.assertEqual(find_rotation_count([2, 4, 6, 8, 10, 12, 1], 1), 6)

    def test_empty_array(self):
        self.assertEqual(find_rotation_count([]), -1)

    def test_single_element_array(self):
        self.assertEqual(find_rotation_count([1]), -1)

    def test_sorted_array(self):
        self.assertEqual(find_rotation_count([0, 1, 2, 3, 4]), -1)

    def test_reversed_array(self):
        self.assertEqual(find_rotation_count([7, 6, 5, 4, 3, 2, 1]), 0)

    def test_rotated_array_with_duplicates(self):
        self.assertEqual(find_rotation_count([1, 0, 1, 2, 1, 3]), 3)
