import unittest
from mbpp_51_code import check_equilateral

class TestCheckEquilateral(unittest.TestCase):

    def test_all_equal(self):
        self.assertTrue(check_equilateral(5,5,5))

    def test_not_all_equal(self):
        self.assertFalse(check_equilateral(3,4,5))

    def test_negative_values(self):
        self.assertFalse(check_equilateral(-1,-1,-1))

    def test_zero(self):
        self.assertFalse(check_equilateral(0,0,0))

    def test_positive_values(self):
        self.assertTrue(check_equilateral(1,1,1))

    def test_mixed_values(self):
        self.assertFalse(check_equilateral(1,2,3))
