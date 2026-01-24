import unittest
from mbpp_382_code import find_rotation_count

class TestFindRotationCount(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_rotation_count([4, 5, 6, 7, 0, 1, 2]), 4)

    def test_already_sorted(self):
        self.assertEqual(find_rotation_count([0, 1, 2, 4, 5, 6, 7]), 0)

    def test_single_element(self):
        self.assertEqual(find_rotation_count([1]), 0)

    def test_empty_list(self):
        self.assertEqual(find_rotation_count([]), -1)

    def test_duplicate_elements(self):
        self.assertEqual(find_rotation_count([4, 5, 6, 7, 0, 0, 1, 2]), 5)

    def test_large_numbers(self):
        self.assertEqual(find_rotation_count([100, 200, 300, 400, 50, 60, 70]), 4)

    def test_negative_numbers(self):
        self.assertEqual(find_rotation_count([-4, -3, -2, -1, 0, 1, 2]), 4)
