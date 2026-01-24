import unittest
from mbpp_382_code import find_rotation_count

class TestFindRotationCount(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(find_rotation_count([15, 18, 2, 3, 6, 12]), 2)

    def test_already_sorted(self):
        self.assertEqual(find_rotation_count([2, 3, 6, 12, 15, 18]), 0)

    def test_single_element(self):
        self.assertEqual(find_rotation_count([1]), 0)

    def test_empty_list(self):
        self.assertEqual(find_rotation_count([]), -1)

    def test_duplicates(self):
        self.assertEqual(find_rotation_count([15, 15, 15, 2, 3, 3, 6, 6, 12, 12]), 3)
