import unittest
from mbpp_150_code import does_Contain_B

class TestDoesContainB(unittest.TestCase):

    def test_equal_values(self):
        self.assertTrue(does_Contain_B(1, 1, 1))

    def test_non_equal_values(self):
        self.assertFalse(does_Contain_B(1, 2, 3))

    def test_non_equal_values_with_common_divisor(self):
        self.assertTrue(does_Contain_B(2, 4, 2))

    def test_non_equal_values_without_common_divisor(self):
        self.assertFalse(does_Contain_B(1, 2, 3))

    def test_equal_values_with_common_divisor(self):
        self.assertTrue(does_Contain_B(2, 2, 2))

    def test_non_equal_values_with_common_divisor(self):
        self.assertTrue(does_Contain_B(2, 4, 2))

    def test_non_equal_values_without_common_divisor(self):
        self.assertFalse(does_Contain_B(1, 2, 3))
