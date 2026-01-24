import unittest
from mbpp_509_code import average_Odd

class TestAverageOdd(unittest.TestCase):
    def test_average_odd_positive_numbers(self):
        self.assertEqual(average_Odd(5), 3)
        self.assertEqual(average_Odd(9), 5)
        self.assertEqual(average_Odd(15), 7)

    def test_average_odd_zero(self):
        self.assertEqual(average_Odd(0), -1)

    def test_average_odd_negative_number(self):
        self.assertEqual(average_Odd(-1), "Invalid Input")

    def test_average_odd_even_number(self):
        self.assertEqual(average_Odd(2), "Invalid Input")
        self.assertEqual(average_Odd(4), "Invalid Input")
