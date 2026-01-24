import unittest
from mbpp_521_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):

    def test_simple_isosceles(self):
        self.assertTrue(check_isosceles(1, 1, 1))
        self.assertTrue(check_isosceles(2, 2, 2))
        self.assertTrue(check_isosceles(3, 3, 3))

    def test_edge_cases(self):
        self.assertFalse(check_isosceles(1, 1, 2))
        self.assertFalse(check_isosceles(1, 2, 1))
        self.assertFalse(check_isosceles(2, 1, 1))
        self.assertFalse(check_isosceles(2, 2, 3))
        self.assertFalse(check_isosceles(3, 2, 2))
        self.assertFalse(check_isosceles(2, 3, 2))

    def test_boundary_cases(self):
        self.assertFalse(check_isosceles(0, 0, 0))
        self.assertFalse(check_isosceles(0, 0, 1))
        self.assertFalse(check_isosceles(1, 0, 0))
        self.assertFalse(check_isosceles(1, 1, 0))
        self.assertFalse(check_isosceles(0, 1, 1))
        self.assertFalse(check_isosceles(1, 0, 1))
        self.assertFalse(check_isosceles(1, 1, 0))

        self.assertTrue(check_isosceles(1, 1, 2))
        self.assertTrue(check_isosceles(1, 2, 1))
        self.assertTrue(check_isosceles(2, 1, 1))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, check_isosceles, 'a', 'b', 'c')
        self.assertRaises(TypeError, check_isosceles, 1, 'b', 'c')
        self.assertRaises(TypeError, check_isosceles, 1, 2, 'c')
