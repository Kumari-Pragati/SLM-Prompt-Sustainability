import unittest
from mbpp_382_code import find_rotation_count

class TestFindRotationCount(unittest.TestCase):

    def test_find_rotation_count(self):
        self.assertEqual(find_rotation_count([4, 5, 6, 7, 8, 9, 1, 2, 3]), 6)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9]), -1)
        self.assertEqual(find_rotation_count([9, 1, 2, 3, 4, 5, 6, 7, 8]), 0)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]), 9)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]), 9)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2]), 9)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]), 9)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4]), 9)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]), 9)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6]), 9)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7]), 9)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8]), 9)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 9)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]), 9)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2]), 9)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]), 9)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4]), 9)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]), 9)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7,