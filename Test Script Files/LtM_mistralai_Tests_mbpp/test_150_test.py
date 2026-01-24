import unittest
from mbpp_150_code import does_Contain_B

class TestDoesContainB(unittest.TestCase):

    def test_simple_equal_strings(self):
        self.assertTrue(does_Contain_B('a', 'a', 1))

    def test_simple_different_strings(self):
        self.assertFalse(does_Contain_B('a', 'b', 1))

    def test_simple_equal_integers(self):
        self.assertTrue(does_Contain_B(5, 5, 1))

    def test_simple_different_integers(self):
        self.assertFalse(does_Contain_B(5, 6, 1))

    def test_simple_equal_floats(self):
        self.assertTrue(does_Contain_B(5.0, 5.0, 1))

    def test_simple_different_floats(self):
        self.assertFalse(does_Contain_B(5.0, 6.0, 1))

    def test_edge_case_zero_difference(self):
        self.assertTrue(does_Contain_B(1, 1, 1))

    def test_edge_case_zero_product(self):
        self.assertFalse(does_Contain_B(1, 0, 1))

    def test_edge_case_non_integer_division(self):
        self.assertFalse(does_Contain_B(1, 2.5, 1))

    def test_complex_case_negative_numbers(self):
        self.assertTrue(does_Contain_B(-1, -2, 1))

    def test_complex_case_negative_product(self):
        self.assertTrue(does_Contain_B(-1, -2, -1))
