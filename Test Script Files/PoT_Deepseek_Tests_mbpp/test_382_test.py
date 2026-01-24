import unittest
from mbpp_382_code import find_rotation_count

class TestFindRotationCount(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_rotation_count([15, 18, 2, 3, 6, 12]), 2)
        self.assertEqual(find_rotation_count([7, 9, 11, 12, 5]), 4)

    def test_edge_cases(self):
        self.assertEqual(find_rotation_count([1]), 0)
        self.assertEqual(find_rotation_count([1, 2]), 0)

    def test_boundary_cases(self):
        self.assertEqual(find_rotation_count([2, 1]), 1)
        self.assertEqual(find_rotation_count([3, 2, 1]), 0)
        self.assertEqual(find_rotation_count([4, 5, 6, 7, 8, 9, 1, 2, 3]), 6)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_rotation_count(None)
        with self.assertRaises(TypeError):
            find_rotation_count(123)
        with self.assertRaises(TypeError):
            find_rotation_count('123')
        with self.assertRaises(TypeError):
            find_rotation_count([1, 2, 'a'])
