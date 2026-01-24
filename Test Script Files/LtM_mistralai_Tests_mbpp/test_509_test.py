import unittest
from mbpp_509_code import average_Odd

class TestAverageOdd(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(average_Odd(3), 2)
        self.assertEqual(average_Odd(5), 5)
        self.assertEqual(average_Odd(7), 7)

    def test_edge_and_boundary(self):
        self.assertEqual(average_Odd(1), 0)
        self.assertEqual(average_Odd(2), "Invalid Input")
        self.assertEqual(average_Odd(4), 2)
        self.assertEqual(average_Odd(6), 3)
        self.assertEqual(average_Odd(8), 4)

    def test_complex_input(self):
        self.assertEqual(average_Odd(9), 6)
        self.assertEqual(average_Odd(11), 10)
        self.assertEqual(average_Odd(13), 13)
        self.assertEqual(average_Odd(15), 9)
        self.assertEqual(average_Odd(17), 15)
