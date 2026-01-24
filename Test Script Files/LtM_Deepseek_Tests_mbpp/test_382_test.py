import unittest
from mbpp_382_code import find_rotation_count

class TestFindRotationCount(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5]), 0)
        self.assertEqual(find_rotation_count([3, 4, 5, 1, 2]), 3)

    def test_edge_conditions(self):
        self.assertEqual(find_rotation_count([1]), -1)
        self.assertEqual(find_rotation_count([]), -1)
        self.assertEqual(find_rotation_count([5, 4, 3, 2, 1]), 4)

    def test_complex_cases(self):
        self.assertEqual(find_rotation_count([4, 5, 1, 2, 3]), 2)
        self.assertEqual(find_rotation_count([2, 1, 3, 4, 5]), 1)
        self.assertEqual(find_rotation_count([5, 1, 2, 3, 4]), 1)
        self.assertEqual(find_rotation_count([3, 4, 5, 1, 2]), 3)
