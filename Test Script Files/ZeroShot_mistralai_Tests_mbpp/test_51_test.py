import unittest
from mbpp_51_code import check_equilateral

class TestCheckEquilateral(unittest.TestCase):

    def test_equilateral_triangle(self):
        self.assertTrue(check_equilateral(3, 3, 3))

    def test_not_equilateral_triangle(self):
        self.assertFalse(check_equilateral(3, 4, 5))
        self.assertFalse(check_equilateral(3, 3, 4))
        self.assertFalse(check_equilateral(4, 3, 3))

    def test_invalid_input(self):
        self.assertRaises(TypeError, check_equilateral, 'a', 'b', 'c')
        self.assertRaises(TypeError, check_equilateral, 3, 'b', 'c')
        self.assertRaises(TypeError, check_equilateral, 3, 4, 'c')
