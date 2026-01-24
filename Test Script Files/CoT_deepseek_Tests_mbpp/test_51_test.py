import unittest
from mbpp_51_code import check_equilateral

class TestCheckEquilateral(unittest.TestCase):

    def test_all_equal_sides(self):
        self.assertTrue(check_equilateral(3, 3, 3))

    def test_different_sides(self):
        self.assertFalse(check_equilateral(3, 4, 5))

    def test_zero_sides(self):
        self.assertFalse(check_equilateral(0, 0, 0))

    def test_negative_sides(self):
        self.assertFalse(check_equilateral(-1, -1, -1))

    def test_one_zero_side(self):
        self.assertFalse(check_equilateral(0, 3, 3))

    def test_one_negative_side(self):
        self.assertFalse(check_equilateral(-1, 3, 3))

    def test_one_positive_one_negative_side(self):
        self.assertFalse(check_equilateral(1, -1, 1))

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            check_equilateral('a', 'b', 'c')
