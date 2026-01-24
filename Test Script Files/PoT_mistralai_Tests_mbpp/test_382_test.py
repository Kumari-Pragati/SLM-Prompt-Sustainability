import unittest
from mbpp_382_code import find_rotation_count

class TestFindRotationCount(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_rotation_count([0, 1, 2, 4, 5, 6, 7]), 0)
        self.assertEqual(find_rotation_n_times([0, 2, 1], n=2), 1)
        self.assertEqual(find_rotation_n_times([3, 4, 5, 6], n=2), 6)
        self.assertEqual(find_rotation_count([10, 11, 12, 1, 2, 3, 4]), 5)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(find_rotation_count([]), -1)
        self.assertEqual(find_rotation_count([1]), -1)
        self.assertEqual(find_rotation_count([1, 1]), -1)
        self.assertEqual(find_rotation_count([1, 2, 1]), -1)
        self.assertEqual(find_rotation_count([1, 2, 1, 0]), 3)
        self.assertEqual(find_rotation_count([1, 2, 1, 0, 1]), 4)
        self.assertEqual(find_rotation_count([1, 2, 1, 0, 1, 2]), -1)
        self.assertEqual(find_rotation_count([1, 2, 1, 0, 1, 2, 3]), 7)
