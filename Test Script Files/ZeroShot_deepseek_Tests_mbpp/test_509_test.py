import unittest
from mbpp_509_code import average_Odd

class TestAverageOdd(unittest.TestCase):

    def test_average_Odd(self):
        self.assertEqual(average_Odd(7), 4)
        self.assertEqual(average_Odd(9), 5)
        self.assertEqual(average_Odd(11), 6)
        self.assertEqual(average_Odd(13), 7)
        self.assertEqual(average_Odd(15), 8)
        self.assertEqual(average_Odd(17), 9)
        self.assertEqual(average_Odd(19), 10)
        self.assertEqual(average_Odd(21), 11)
        self.assertEqual(average_Odd(23), 12)
        self.assertEqual(average_Odd(25), 13)
        self.assertEqual(average_Odd(0), "Invalid Input")
        self.assertEqual(average_Odd(-1), "Invalid Input")
        self.assertEqual(average_Odd(2), "Invalid Input")
