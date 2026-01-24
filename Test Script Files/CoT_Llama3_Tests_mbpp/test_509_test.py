import unittest
from mbpp_509_code import average_Odd

class TestAverageOdd(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(average_Odd(10), 5)

    def test_invalid_input_even(self):
        self.assertEqual(average_Odd(4), "Invalid Input")

    def test_invalid_input_negative(self):
        self.assertEqual(average_Odd(-10), "Invalid Input")

    def test_edge_case_zero(self):
        self.assertEqual(average_Odd(0), 0)

    def test_edge_case_one(self):
        self.assertEqual(average_Odd(1), 1)

    def test_edge_case_two(self):
        self.assertEqual(average_Odd(2), "Invalid Input")

    def test_edge_case_large(self):
        self.assertEqual(average_Odd(100), 50)

    def test_edge_case_negative_large(self):
        self.assertEqual(average_Odd(-100), "Invalid Input")
