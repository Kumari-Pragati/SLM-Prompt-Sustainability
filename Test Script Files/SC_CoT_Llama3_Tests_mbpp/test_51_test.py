import unittest
from mbpp_51_code import check_equilateral

class TestCheckEquilateral(unittest.TestCase):
    def test_equilateral(self):
        self.assertTrue(check_equilateral(1, 1, 1))
    def test_non_equilateral(self):
        self.assertFalse(check_equilateral(1, 2, 3))
    def test_equilateral_with_negative_numbers(self):
        self.assertTrue(check_equilateral(-1, -1, -1))
    def test_equilateral_with_zero(self):
        self.assertFalse(check_equilateral(0, 0, 0))
    def test_non_equilateral_with_zero(self):
        self.assertFalse(check_equilateral(0, 1, 2))
    def test_non_equilateral_with_negative_numbers(self):
        self.assertFalse(check_equilateral(-1, 2, 3))
    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            check_equilateral('a', 1, 2)
