import unittest
from mbpp_327_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_isosceles(3, 3, 2))

    def test_edge_case(self):
        self.assertTrue(check_isosceles(0, 0, 0))

    def test_boundary_case(self):
        self.assertTrue(check_isosceles(1, 1, 1))
        self.assertTrue(check_isosceles(1, 2, 2))

    def test_corner_case(self):
        self.assertTrue(check_isosceles(1, 1, 2))
        self.assertFalse(check_isosceles(1, 2, 3))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_isosceles("a", 1, 1)
        with self.assertRaises(TypeError):
            check_isosceles(1, "a", 1)
        with self.assertRaises(TypeError):
            check_isosceles(1, 1, "a")
