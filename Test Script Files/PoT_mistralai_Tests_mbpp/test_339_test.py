import unittest
from mbpp_339_code import find_Divisor

class TestFindDivisor(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Divisor(6, 3), 3)
        self.assertEqual(find_Divisor(10, 2), 2)
        self.assertEqual(find_Divisor(12, 4), 4)

    def test_edge_case_x_is_1(self):
        self.assertEqual(find_Divisor(1, 2), 2)

    def test_edge_case_y_is_1(self):
        self.assertEqual(find_Divisor(2, 1), 2)

    def test_boundary_case_x_is_0(self):
        self.assertEqual(find_Divisor(0, 2), None)

    def test_boundary_case_y_is_0(self):
        self.assertEqual(find_Divisor(2, 0), None)
