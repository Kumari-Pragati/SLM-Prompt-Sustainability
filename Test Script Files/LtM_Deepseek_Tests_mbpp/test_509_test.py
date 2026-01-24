import unittest
from mbpp_509_code import average_Odd

class TestAverageOdd(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(average_Odd(7), 5)

    def test_edge_boundary_conditions(self):
        self.assertEqual(average_Odd(1), 1)
        self.assertEqual(average_Odd(3), "Invalid Input")
        self.assertEqual(average_Odd(0), "Invalid Input")
        self.assertEqual(average_Odd(-1), "Invalid Input")

    def test_more_complex_cases(self):
        self.assertEqual(average_Odd(9), 7)
        self.assertEqual(average_Odd(15), 11)
