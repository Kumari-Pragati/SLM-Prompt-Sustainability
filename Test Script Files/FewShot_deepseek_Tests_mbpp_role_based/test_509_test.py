import unittest
from mbpp_509_code import average_Odd

class TestAverageOdd(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(average_Odd(7), 5)

    def test_boundary_condition(self):
        self.assertEqual(average_Odd(1), 1)

    def test_edge_condition(self):
        self.assertEqual(average_Odd(2), "Invalid Input")
        self.assertEqual(average_Odd(0), "Invalid Input")
        self.assertEqual(average_Odd(-1), "Invalid Input")

    def test_invalid_input(self):
        self.assertEqual(average_Odd("7"), "Invalid Input")
        self.assertEqual(average_Odd(None), "Invalid Input")
        self.assertEqual(average_Odd([1,2,3]), "Invalid Input")
