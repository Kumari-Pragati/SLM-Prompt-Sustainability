import unittest
from mbpp_509_code import average_Odd

class TestAverageOdd(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(average_Odd(7), 7)
        self.assertEqual(average_Odd(9), 9)
        self.assertEqual(average_Odd(11), 11)

    def test_edge_cases(self):
        self.assertEqual(average_Odd(1), 1)
        self.assertEqual(average_Odd(2), "Invalid Input")

    def test_boundary_cases(self):
        self.assertEqual(average_Odd(3), 3)
        self.assertEqual(average_Odd(5), 5)
        self.assertEqual(average_Odd(0), "Invalid Input")
        self.assertEqual(average_Odd(-1), "Invalid Input")

    def test_invalid_input(self):
        self.assertEqual(average_Odd("abc"), "Invalid Input")
        self.assertEqual(average_Odd(None), "Invalid Input")
        self.assertEqual(average_Odd([1,2,3]), "Invalid Input")
