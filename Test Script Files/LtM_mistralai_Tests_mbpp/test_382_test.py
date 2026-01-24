import unittest
from mbpp_382_code import find_rotation_count

class TestFindRotationCount(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(find_rotation_count([0, 1, 2, 4, 5, 6, 7]), 0)
        self.assertEqual(find_rotation_count([4, 5, 6, 7, 0, 1, 2]), 6)
        self.assertEqual(find_rotation_count([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]), 0)

    def test_edge_cases(self):
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5]), -1)
        self.assertEqual(find_rotation_count([5, 4, 3, 2, 1]), 4)
        self.assertEqual(find_rotation_count([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]), 11)
        self.assertEqual(find_rotation_count([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]), 20)

    def test_boundary_conditions(self):
        self.assertEqual(find_rotation_count([0]), 0)
        self.assertEqual(find_rotation_count([1]), 1)
        self.assertEqual(find_rotation_count([2]), 2)
        self.assertEqual(find_rotation_count([3]), 3)
        self.assertEqual(find_rotation_count([4]), 4)
        self.assertEqual(find_rotation_count([5]), 5)
