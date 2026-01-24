import unittest
from mbpp_327_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):

    def test_isosceles_true(self):
        self.assertTrue(check_isosceles(3, 3, 3))

    def test_isosceles_false(self):
        self.assertFalse(check_isosceles(1, 2, 3))

    def test_isosceles_equal(self):
        self.assertTrue(check_isosceles(2, 2, 4))

    def test_isosceles_reverse(self):
        self.assertTrue(check_isosceles(4, 2, 2))

    def test_isosceles_all_equal(self):
        self.assertTrue(check_isosceles(5, 5, 5))

    def test_isosceles_all_diff(self):
        self.assertFalse(check_isosceles(1, 2, 3))
