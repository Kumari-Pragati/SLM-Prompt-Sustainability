import unittest
from mbpp_692_code import last_Two_Digits

class TestLastTwoDigits(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(last_Two_Digits(1), 1)
        self.assertEqual(last_Two_Digits(2), 2)
        self.assertEqual(last_Two_Digits(3), 3)
        self.assertEqual(last_Two_Digits(4), 4)
        self.assertEqual(last_Two_Digits(5), 5)

    def test_edge_cases(self):
        self.assertEqual(last_Two_Digits(0), 0)
        self.assertEqual(last_Two_Digits(9), 9)
        self.assertEqual(last_Two_Digits(10), 0)
        self.assertEqual(last_Two_Digits(99), 9)

    def test_complex_input(self):
        self.assertEqual(last_Two_Digits(100), 0)
        self.assertEqual(last_Two_Digits(101), 1)
        self.assertEqual(last_Two_Digits(999), 9)
        self.assertEqual(last_Two_Digits(1000), 0)
