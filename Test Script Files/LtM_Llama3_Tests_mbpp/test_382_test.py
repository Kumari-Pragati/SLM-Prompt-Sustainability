import unittest
from mbpp_382_code import find_rotation_count

class TestFindRotationCount(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5]), 0)
        self.assertEqual(find_rotation_count([5, 1, 2, 3, 4]), 0)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6]), 0)
        self.assertEqual(find_rotation_count([6, 5, 4, 3, 2, 1]), 0)

    def test_edge(self):
        self.assertEqual(find_rotation_count([1]), 0)
        self.assertEqual(find_rotation_count([1, 2]), 0)
        self.assertEqual(find_rotation_count([2, 1]), 0)
        self.assertEqual(find_rotation_count([1, 2, 3]), 0)
        self.assertEqual(find_rotation_count([3, 2, 1]), 0)

    def test_rotation(self):
        self.assertEqual(find_rotation_count([5, 1, 2, 3, 4]), 1)
        self.assertEqual(find_rotation_count([4, 5, 1, 2, 3]), 1)
        self.assertEqual(find_rotation_count([3, 4, 5, 1, 2]), 1)
        self.assertEqual(find_rotation_count([2, 3, 4, 5, 1]), 1)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5]), -1)

    def test_invalid(self):
        self.assertEqual(find_rotation_count([]), -1)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), -1)
