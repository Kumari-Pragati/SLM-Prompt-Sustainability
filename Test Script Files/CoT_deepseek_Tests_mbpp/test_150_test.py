import unittest
from mbpp_150_code import does_Contain_B

class TestDoesContainB(unittest.TestCase):

    def test_equal_numbers(self):
        self.assertTrue(does_Contain_B(5, 5, 0))

    def test_positive_difference_multiple_of_c(self):
        self.assertTrue(does_Contain_B(2, 10, 3))

    def test_positive_difference_not_multiple_of_c(self):
        self.assertFalse(does_Contain_B(2, 10, 2))

    def test_negative_difference_multiple_of_c(self):
        self.assertTrue(does_Contain_B(10, 2, 3))

    def test_negative_difference_not_multiple_of_c(self):
        self.assertFalse(does_Contain_B(10, 2, 2))

    def test_zero_c(self):
        self.assertTrue(does_Contain_B(5, 5, 0))

    def test_equal_a_and_b(self):
        self.assertTrue(does_Contain_B(5, 5, 3))

    def test_a_greater_than_b(self):
        self.assertFalse(does_Contain_B(10, 5, 3))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            does_Contain_B("a", 5, 3)

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            does_Contain_B(10, 5, 0)
