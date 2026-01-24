import unittest
from mbpp_382_code import find_rotation_count

class TestFindRotationCount(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_rotation_count([15, 18, 2, 3, 6, 12]), 2)
        self.assertEqual(find_rotation_count([7, 9, 11, 12, 5]), 4)
        self.assertEqual(find_rotation_count([4, 5, 6, 1, 2, 3]), 3)

    def test_edge_cases(self):
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5]), 0)
        self.assertEqual(find_rotation_count([5, 1, 2, 3, 4]), 1)
        self.assertEqual(find_rotation_count([4, 5, 6, 7, 8, 9, 1, 2, 3]), 6)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            find_rotation_count("1, 2, 3, 4, 5")
        with self.assertRaises(TypeError):
            find_rotation_count(12345)
        with self.assertRaises(TypeError):
            find_rotation_count([1, 2, "3", 4, 5])
