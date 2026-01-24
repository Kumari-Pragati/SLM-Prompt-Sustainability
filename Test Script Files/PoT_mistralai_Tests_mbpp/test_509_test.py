import unittest
from mbpp_509_code import average_Odd

class TestAverageOdd(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(average_Odd(5), 3)
        self.assertEqual(average_Odd(9), 7)
        self.assertEqual(average_Odd(15), 9)

    def test_edge_case(self):
        self.assertEqual(average_Odd(1), 1)
        self.assertEqual(average_Odd(3), 1)
        self.assertEqual(average_Odd(7), 1)

    def test_boundary_case(self):
        self.assertEqual(average_Odd(0), "Invalid Input")
        self.assertEqual(average_Odd(2), "Invalid Input")
        self.assertEqual(average_Odd(4), "Invalid Input")
