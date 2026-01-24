import unittest
from mbpp_509_code import average_Odd

class TestAverageOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(average_Odd(7), 5)

    def test_edge_case(self):
        self.assertEqual(average_Odd(1), 1)

    def test_boundary_case(self):
        self.assertEqual(average_Odd(2), "Invalid Input")
        self.assertEqual(average_Odd(0), "Invalid Input")
        self.assertEqual(average_Odd(-1), "Invalid Input")

    def test_special_case(self):
        self.assertEqual(average_Odd(9), 7)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            average_Odd("invalid")
