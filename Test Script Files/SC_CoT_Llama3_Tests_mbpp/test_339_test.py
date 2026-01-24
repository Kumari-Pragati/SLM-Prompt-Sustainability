import unittest
from mbpp_339_code import find_Divisor

class TestFindDivisor(unittest.TestCase):

    def test_equal_inputs(self):
        self.assertEqual(find_Divisor(5,5), 5)

    def test_non_equal_inputs(self):
        self.assertEqual(find_Divisor(5,3), 2)

    def test_edge_case_x_zero(self):
        with self.assertRaises(TypeError):
            find_Divisor(0,3)

    def test_edge_case_y_zero(self):
        with self.assertRaises(TypeError):
            find_Divisor(3,0)

    def test_edge_case_x_negative(self):
        with self.assertRaises(TypeError):
            find_Divisor(-5,3)

    def test_edge_case_y_negative(self):
        with self.assertRaises(TypeError):
            find_Divisor(3,-5)

    def test_edge_case_x_and_y_negative(self):
        with self.assertRaises(TypeError):
            find_Divisor(-5,-3)
