import unittest
from mbpp_695_code import zip_longest
from 695_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertFalse(check_greater((1, 2, 3), (2, 1, 3)))
        self.assertFalse(check_greater((1, 2, 3), (1, 2, 4)))
        self.assertTrue(check_greater((1, 2, 3), (1, 3, 5)))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(check_greater([], []))
        self.assertFalse(check_greater([1], []))
        self.assertTrue(check_greater([1], [1]))
        self.assertTrue(check_greater([1, 2, 3], [1, 2, 3]))
        self.assertTrue(check_greater([1, 2, 3], [1, 2, 3, 4]))
        self.assertFalse(check_greater([1, 2, 3], [1, 2, 3, 4, 5]))

    def test_special_or_corner_cases(self):
        self.assertFalse(check_greater((1, 2, 3), (2, 1, 3, 4)))
        self.assertFalse(check_greater((1, 2, 3), (2, 1, 3, 4, 5)))
        self.assertTrue(check_greater((1, 2, 3), (2, 3, 1)))
        self.assertTrue(check_greater((1, 2, 3), (3, 2, 1)))
        self.assertFalse(check_greater((1, 2, 3), (3, 2, 1, 4)))
        self.assertFalse(check_greater((1, 2, 3), (3, 2, 1, 4, 5)))
