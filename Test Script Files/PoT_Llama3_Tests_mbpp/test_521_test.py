import unittest
from mbpp_521_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_isosceles(3, 3, 5))

    def test_edge_case_equal_sides(self):
        self.assertTrue(check_isosceles(3, 3, 3))

    def test_edge_case_all_sides_equal(self):
        self.assertTrue(check_isosceles(3, 3, 3))

    def test_edge_case_all_sides_not_equal(self):
        self.assertFalse(check_isosceles(3, 4, 5))

    def test_edge_case_one_side_zero(self):
        with self.assertRaises(TypeError):
            check_isosceles(0, 3, 4)

    def test_edge_case_one_side_negative(self):
        with self.assertRaises(TypeError):
            check_isosceles(-1, 3, 4)

    def test_edge_case_all_sides_negative(self):
        with self.assertRaises(TypeError):
            check_isosceles(-1, -2, -3)

    def test_edge_case_all_sides_zero(self):
        with self.assertRaises(TypeError):
            check_isosceles(0, 0, 0)
