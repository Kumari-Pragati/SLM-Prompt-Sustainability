import unittest
from mbpp_51_code import check_equilateral

class TestCheckEquilateral(unittest.TestCase):
    def test_equilateral(self):
        self.assertTrue(check_equilateral(1,1,1))
    def test_non_equilateral(self):
        self.assertFalse(check_equilateral(1,2,3))
    def test_single_value(self):
        self.assertFalse(check_equilateral(1,1,2))
    def test_negative_values(self):
        self.assertFalse(check_equilateral(-1,-1,-1))
    def test_zero_values(self):
        self.assertFalse(check_equilateral(0,0,0))
