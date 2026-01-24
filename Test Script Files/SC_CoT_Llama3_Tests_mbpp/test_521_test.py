import unittest
from mbpp_521_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):

    def test_isosceles_true(self):
        self.assertTrue(check_isosceles(3,3,3))

    def test_isosceles_false(self):
        self.assertFalse(check_isosceles(1,2,3))

    def test_isosceles_edge_case1(self):
        self.assertTrue(check_isosceles(2,2,3))

    def test_isosceles_edge_case2(self):
        self.assertFalse(check_isosceles(1,1,2))

    def test_isosceles_edge_case3(self):
        self.assertTrue(check_isosceles(3,3,1))

    def test_isosceles_invalid_input1(self):
        with self.assertRaises(TypeError):
            check_isosceles("a", 2, 3)

    def test_isosceles_invalid_input2(self):
        with self.assertRaises(TypeError):
            check_isosceles(1, "b", 3)

    def test_isosceles_invalid_input3(self):
        with self.assertRaises(TypeError):
            check_isosceles(1, 2, "c")
