import unittest
from mbpp_150_code import does_Contain_B

class TestDoesContainB(unittest.TestCase):

    def test_equal_numbers(self):
        self.assertTrue(does_Contain_B(5, 5, 0))

    def test_positive_difference_multiple_of_c(self):
        self.assertTrue(does_Contain_B(2, 10, 4))

    def test_positive_difference_not_multiple_of_c(self):
        self.assertFalse(does_Contain_B(2, 10, 3))

    def test_negative_difference(self):
        self.assertFalse(does_Contain_B(10, 2, 4))

    def test_zero_c(self):
        self.assertTrue(does_Contain_B(5, 5, 0))
