import unittest
from mbpp_51_code import check_equilateral

class TestCheckEquilateral(unittest.TestCase):

    def test_simple_equilateral(self):
        self.assertTrue(check_equilateral(3, 3, 3))

    def test_zero_equilateral(self):
        self.assertTrue(check_equilateral(0, 0, 0))

    def test_positive_negative_equilateral(self):
        self.assertTrue(check_equilateral(-3, -3, -3))

    def test_edge_case_one_equal(self):
        self.assertTrue(check_equilateral(3, 3, 2))

    def test_edge_case_two_equal(self):
        self.assertTrue(check_equilateral(3, 2, 3))

    def test_edge_case_three_equal(self):
        self.assertTrue(check_equilateral(2, 3, 3))

    def test_edge_case_all_different(self):
        self.assertFalse(check_equilateral(3, 4, 5))

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            check_equilateral()
