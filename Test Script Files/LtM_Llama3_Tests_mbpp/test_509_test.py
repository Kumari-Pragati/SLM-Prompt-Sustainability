import unittest
from mbpp_509_code import average_Odd

class TestAverageOdd(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(average_Odd(10), 5)
        self.assertEqual(average_Odd(20), 10)
        self.assertEqual(average_Odd(30), 15)

    def test_edge_case(self):
        self.assertEqual(average_Odd(0), -1)
        self.assertEqual(average_Odd(1), -1)
        self.assertEqual(average_Odd(2), 1)

    def test_invalid_input(self):
        self.assertEqual(average_Odd(3), "Invalid Input")
        self.assertEqual(average_Odd(4), "Invalid Input")
        self.assertEqual(average_Odd(5), "Invalid Input")

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            average_Odd(0)
