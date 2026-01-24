import unittest
from mbpp_509_code import average_Odd

class TestAverageOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(average_Odd(7), 4)

    def test_edge_case_with_one(self):
        self.assertEqual(average_Odd(1), 1)

    def test_edge_case_with_zero(self):
        self.assertEqual(average_Odd(0), "Invalid Input")

    def test_edge_case_with_negative(self):
        self.assertEqual(average_Odd(-1), "Invalid Input")

    def test_explicitly_handled_error_case(self):
        self.assertEqual(average_Odd(8), "Invalid Input")
