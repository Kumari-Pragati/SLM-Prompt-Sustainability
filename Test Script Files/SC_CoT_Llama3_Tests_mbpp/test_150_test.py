import unittest
from mbpp_150_code import does_Contain_B

class TestDoesContainB(unittest.TestCase):
    def test_equal(self):
        self.assertTrue(does_Contain_B(1, 1, 1))

    def test_diff_with_multiple_of_c(self):
        self.assertTrue(does_Contain_B(1, 2, 2))

    def test_diff_with_multiple_of_c_negative(self):
        self.assertTrue(does_Contain_B(-1, -2, 2))

    def test_diff_with_multiple_of_c_zero(self):
        self.assertFalse(does_Contain_B(0, 0, 1))

    def test_diff_with_multiple_of_c_zero_negative(self):
        self.assertFalse(does_Contain_B(0, 0, -1))

    def test_diff_with_non_multiple_of_c(self):
        self.assertFalse(does_Contain_B(1, 2, 3))

    def test_diff_with_non_multiple_of_c_negative(self):
        self.assertFalse(does_Contain_B(-1, -2, 3))

    def test_diff_with_non_multiple_of_c_zero(self):
        self.assertFalse(does_Contain_B(0, 0, 0))

    def test_diff_with_non_multiple_of_c_zero_negative(self):
        self.assertFalse(does_Contain_B(0, 0, 0))

    def test_equal_negative(self):
        self.assertTrue(does_Contain_B(-1, -1, -1))

    def test_equal_zero(self):
        self.assertFalse(does_Contain_B(0, 0, 0))
