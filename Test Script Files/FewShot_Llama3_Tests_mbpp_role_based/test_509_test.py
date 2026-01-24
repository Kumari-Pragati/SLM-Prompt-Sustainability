import unittest
from mbpp_509_code import average_Odd

class TestAverageOdd(unittest.TestCase):
    def test_average_odd_positive_numbers(self):
        self.assertEqual(average_Odd(10), 5)

    def test_average_odd_zero(self):
        self.assertEqual(average_Odd(0), -1)

    def test_average_odd_negative_numbers(self):
        self.assertEqual(average_Odd(-10), -5)

    def test_average_odd_invalid_input(self):
        self.assertEqual(average_Odd(4), "Invalid Input")

    def test_average_odd_edge_case(self):
        self.assertEqual(average_Odd(1), 1)

    def test_average_odd_edge_case_zero(self):
        self.assertEqual(average_Odd(0), -1)
