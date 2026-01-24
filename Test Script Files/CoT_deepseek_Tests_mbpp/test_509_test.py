import unittest
from mbpp_509_code import average_Odd

class TestAverageOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(average_Odd(7), 5)

    def test_edge_case(self):
        self.assertEqual(average_Odd(1), 1)

    def test_invalid_input(self):
        self.assertEqual(average_Odd(8), "Invalid Input")
        self.assertEqual(average_Odd(0), "Invalid Input")
        self.assertEqual(average_Odd(-1), "Invalid Input")

    def test_boundary_conditions(self):
        self.assertEqual(average_Odd(1), 1)
        self.assertEqual(average_Odd(2), "Invalid Input")
        self.assertEqual(average_Odd(3), 2)
        self.assertEqual(average_Odd(4), "Invalid Input")
        self.assertEqual(average_Odd(5), 4)
        self.assertEqual(average_Odd(6), "Invalid Input")
        self.assertEqual(average_Odd(7), 5)
