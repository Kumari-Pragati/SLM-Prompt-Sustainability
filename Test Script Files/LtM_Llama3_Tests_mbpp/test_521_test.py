import unittest
from mbpp_521_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(check_isosceles(3, 3, 3))
        self.assertTrue(check_isosceles(5, 5, 5))
        self.assertTrue(check_isosceles(7, 7, 7))

    def test_edge_valid(self):
        self.assertTrue(check_isosceles(0, 0, 0))
        self.assertTrue(check_isosceles(1, 1, 1))
        self.assertTrue(check_isosceles(10, 10, 10))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_isosceles('a', 'b', 'c')
        with self.assertRaises(TypeError):
            check_isosceles(1, 'b', 'c')
        with self.assertRaises(TypeError):
            check_isosceles(1, 2, 'c')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            check_isosceles([1, 2, 3], [1, 2, 3], [1, 2, 3])
