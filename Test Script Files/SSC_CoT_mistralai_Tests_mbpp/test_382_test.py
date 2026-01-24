import unittest
from mbpp_382_code import find_rotation_count

class TestFindRotationCount(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(find_rotation_count([4, 5, 6, 7, 8, 1, 2, 3]), 3)
        self.assertEqual(find_rotation_rotation_count([1, 2, 3, 4, 5, 6, 7, 8]), 0)
        self.assertEqual(find_rotation_count([8, 1, 2, 3, 4, 5, 6, 7]), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_rotation_count([1]), 0)
        self.assertEqual(find_rotation_count([1, 1]), 1)
        self.assertEqual(find_rotation_count([1, 2, 1]), 2)
        self.assertEqual(find_rotation_count([1, 2, 3, 1]), 3)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 1]), 4)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 1]), 5)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 1]), 6)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 1]), 7)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 1]), 8)
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]), 9)

        self.assertEqual(find_rotation_count([10, 20, 30, 40, 50, 60, 70, 80, 90, 1]), 10)
        self.assertEqual(find_rotation_count([10, 20, 30, 40, 50, 60, 70, 80, 90, 10]), 0)

    def test_special_cases(self):
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 5, 6, 7]), 5)
        self.assertEqual(find_rotation_count([5, 6, 7, 1, 2, 3, 4]), 5)
        self.assertEqual(find_rotation_count([5, 6, 7, 8, 1, 2, 3, 4]), 8)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, find_rotation_count, [1, 2, 3, "a"])
        self.assertRaises(TypeError, find_rotation_count, [1, 2, 3, [4, 5]])
        self.assertRaises(TypeError, find_rotation_count, [1, 2, 3, (4, 5)])
        self.assertRaises(TypeError, find_rotation_count, [1, 2, 3, None])
