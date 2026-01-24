import unittest
from mbpp_150_code import does_Contain_B

class TestDoesContainB(unittest.TestCase):
    def test_equal_values(self):
        self.assertTrue(does_Contain_B(1, 1, 1))

    def test_non_equal_values(self):
        self.assertFalse(does_Contain_B(1, 2, 3))

    def test_non_equal_values_with_common_divisor(self):
        self.assertTrue(does_Contain_B(4, 6, 2))

    def test_non_equal_values_without_common_divisor(self):
        self.assertFalse(does_Contain_B(4, 5, 2))

    def test_non_equal_values_with_common_divisor_and_zero(self):
        self.assertTrue(does_Contain_B(0, 0, 0))

    def test_non_equal_values_without_common_divisor_and_zero(self):
        self.assertFalse(does_Contain_B(0, 1, 0))
