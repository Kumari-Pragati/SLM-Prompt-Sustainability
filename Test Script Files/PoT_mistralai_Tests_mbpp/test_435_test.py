import unittest
from mbpp_435_code import last_Digit

class TestLastDigit(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(last_Digit(12345), 5)
        self.assertEqual(last_Digit(9876), 6)
        self.assertEqual(last_Digit(0), 0)
        self.assertEqual(last_Digit(10), 0)
        self.assertEqual(last_Digit(100), 0)
        self.assertEqual(last_Digit(-12345), 5)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(last_Digit(0), 0)
        self.assertEqual(last_Digit(1), 1)
        self.assertEqual(last_Digit(9), 9)
        self.assertEqual(last_Digit(1000000), 0)
        self.assertEqual(last_Digit(-1), -1)
        self.assertEqual(last_Digit(-1000000), 0)
