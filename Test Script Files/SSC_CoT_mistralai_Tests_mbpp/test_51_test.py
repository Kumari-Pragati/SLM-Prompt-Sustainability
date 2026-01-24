import unittest
from mbpp_51_code import check_equilateral

class TestCheckEquilateral(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertTrue(check_equilateral(3, 3, 3))

    def test_zero(self):
        self.assertFalse(check_equilateral(0, 0, 0))

    def test_positive_and_negative(self):
        self.assertTrue(check_equilateral(-3, 3, 3))
        self.assertTrue(check_equilateral(3, -3, 3))
        self.assertTrue(check_equilateral(3, 3, -3))

    def test_edge_case_one_equal(self):
        self.assertTrue(check_equilateral(1, 1, 2))
        self.assertTrue(check_equilateral(1, 2, 1))
        self.assertTrue(check_equilateral(2, 1, 1))

    def test_invalid_input(self):
        self.assertRaises(TypeError, check_equilateral, 'a', 1, 1)
        self.assertRaises(TypeError, check_equilateral, 1, 'a', 1)
        self.assertRaises(TypeError, check_equilateral, 1, 1, 'a')
