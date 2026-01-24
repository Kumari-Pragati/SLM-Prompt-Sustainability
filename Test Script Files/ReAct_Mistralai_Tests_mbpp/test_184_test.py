import unittest
from mbpp_184_code import greater_specificnum

class TestGreaterSpecificNum(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(greater_specificnum([], 10))

    def test_single_element_list(self):
        for num in range(10):
            self.assertFalse(greater_specificnum([num], num + 1))
            self.assertTrue(greater_specificnum([num], num))

    def test_positive_numbers(self):
        for num1 in range(10):
            for num2 in range(num1 + 1, 20):
                self.assertTrue(greater_specificnum([num1, num2], num2))

    def test_negative_numbers(self):
        for num1 in range(-10, 0):
            for num2 in range(num1 - 1, -10, -1):
                self.assertTrue(greater_specificnum([num1, num2], num2))

    def test_mixed_numbers(self):
        for num1 in range(-10, 10):
            for num2 in range(-10, 10):
                if num1 > num2:
                    self.assertTrue(greater_specificnum([num1, num2], num2))
                else:
                    self.assertFalse(greater_specificnum([num1, num2], num2))

    def test_zero(self):
        self.assertFalse(greater_specificnum([0], 1))
        self.assertTrue(greater_specificnum([0], 0))
