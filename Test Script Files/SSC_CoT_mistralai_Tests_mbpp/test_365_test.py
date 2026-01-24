import unittest
from mbpp_365_code import count_Digit

class TestCountDigit(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_Digit(12345), 5)
        self.assertEqual(count_Digit(987654321), 10)

    def test_edge_cases(self):
        self.assertEqual(count_Digit(0), 0)
        self.assertEqual(count_Digit(10), 1)
        self.assertEqual(count_Digit(9), 1)
        self.assertEqual(count_Digit(100), 2)
        self.assertEqual(count_Digit(999), 3)
        self.assertEqual(count_Digit(1000), 3)

    def test_negative_input(self):
        self.assertEqual(count_Digit(-12345), 5)

    def test_floating_point_input(self):
        self.assertEqual(count_Digit(12345.0), 5)
        self.assertEqual(count_Digit(-12345.0), 5)
