import unittest
from mbpp_509_code import average_Odd

class TestAverageOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(average_Odd(10), 5)

    def test_edge_case_zero(self):
        self.assertEqual(average_Odd(0), -1)

    def test_edge_case_one(self):
        self.assertEqual(average_Odd(1), -1)

    def test_edge_case_even(self):
        self.assertEqual(average_Odd(4), -1)

    def test_edge_case_negative(self):
        self.assertEqual(average_Odd(-10), -1)

    def test_edge_case_zero_input(self):
        self.assertEqual(average_Odd(0), -1)

    def test_edge_case_invalid_input(self):
        self.assertEqual(average_Odd(5), "Invalid Input")
