import unittest
from mbpp_150_code import does_Contain_B

class TestDoesContainB(unittest.TestCase):
    def test_equal_values(self):
        self.assertTrue(does_Contain_B(1, 1, 1))

    def test_multiple_of_difference(self):
        self.assertTrue(does_Contain_B(1, 2, 1))

    def test_not_multiple_of_difference(self):
        self.assertFalse(does_Contain_B(1, 2, 3))

    def test_zero_difference(self):
        self.assertTrue(does_Contain_B(1, 1, 0))

    def test_zero_c(self):
        self.assertFalse(does_Contain_B(1, 2, 0))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            does_Contain_B('a', 'b', 'c')

    def test_invalid_input_value(self):
        with self.assertRaises(TypeError):
            does_Contain_B(1, 'b', 3)
