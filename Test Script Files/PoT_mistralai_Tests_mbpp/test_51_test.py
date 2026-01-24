import unittest
from mbpp_51_code import check_equilateral

class TestCheckEquilateral(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertTrue(check_equilateral(3, 3, 3))

    def test_non_equilateral_triangle(self):
        self.assertFalse(check_equilateral(3, 4, 5))
        self.assertFalse(check_equilateral(3, 3, 6))
        self.assertFalse(check_equilateral(0, 0, 0))
        self.assertFalse(check_equilateral(-3, -3, -3))
        self.assertFalse(check_equilateral(float('nan'), float('nan'), float('nan')))
        self.assertFalse(check_equilateral(float('inf'), float('inf'), float('inf')))
