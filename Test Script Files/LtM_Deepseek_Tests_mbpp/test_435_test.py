import unittest
from mbpp_435_code import last_Digit

class TestLastDigit(unittest.TestCase):

    # Test for simple / typical inputs
    def test_positive_numbers(self):
        self.assertEqual(last_Digit(123), 3)
        self.assertEqual(last_Digit(98765), 5)

    # Test for edge and boundary conditions
    def test_negative_numbers(self):
        self.assertEqual(last_Digit(-123), 3)
        self.assertEqual(last_Digit(-98765), 5)

    def test_single_digit_numbers(self):
        self.assertEqual(last_Digit(0), 0)
        self.assertEqual(last_Digit(9), 9)

    # Test for more complex or corner cases
    def test_large_numbers(self):
        self.assertEqual(last_Digit(1000000000), 0)
        self.assertEqual(last_Digit(9999999999), 9)
