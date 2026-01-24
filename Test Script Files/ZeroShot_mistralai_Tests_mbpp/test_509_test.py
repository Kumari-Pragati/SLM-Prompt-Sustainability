import unittest
from mbpp_509_code import average_Odd

class TestAverageOdd(unittest.TestCase):

    def test_average_odd_positive_numbers(self):
        self.assertEqual(average_Odd(1), 0)
        self.assertEqual(average_Odd(3), 2)
        self.assertEqual(average_Odd(5), 4)
        self.assertEqual(average_Odd(7), 6)
        self.assertEqual(average_Odd(9), 8)

    def test_average_odd_zero(self):
        self.assertEqual(average_Odd(0), "Invalid Input")

    def test_average_odd_negative_numbers(self):
        self.assertEqual(average_Odd(-1), "Invalid Input")
        self.assertEqual(average_Odd(-3), "Invalid Input")

    def test_average_odd_even_numbers(self):
        self.assertEqual(average_Odd(2), "Invalid Input")
        self.assertEqual(average_Odd(4), "Invalid Input")
        self.assertEqual(average_Odd(6), "Invalid Input")
