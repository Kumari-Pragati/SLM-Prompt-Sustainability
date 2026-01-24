import unittest
from mbpp_382_code import find_rotation_count

class TestFindRotationCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_rotation_count([5, 6, 7, 8, 9, 10, 1, 2, 3, 4]), 5)

    def test_already_sorted(self):
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 0)

    def test_single_element(self):
        self.assertEqual(find_rotation_count([1]), -1)

    def test_empty_list(self):
        self.assertEqual(find_rotation_count([]), -1)

    def test_duplicates(self):
        self.assertEqual(find_rotation_count([5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 4]), 5)

    def test_large_numbers(self):
        self.assertEqual(find_rotation_count([10000, 20000, 30000, 40000, 5000, 6000, 7000, 8000, 9000, 1000]), 4)

    def test_negative_numbers(self):
        self.assertEqual(find_rotation_count([-10, -5, 0, 5, 10, 15, 20, 25, 30, 35]), 5)
