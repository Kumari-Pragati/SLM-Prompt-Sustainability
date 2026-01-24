import unittest
from mbpp_692_code import last_Two_Digits

class TestLastTwoDigits(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(last_Two_Digits(11), 1)
        self.assertEqual(last_Two_Digits(22), 2)
        self.assertEqual(last_Two_Digits(33), 3)
        self.assertEqual(last_Two_Digits(44), 4)
        self.assertEqual(last_Two_Digits(55), 5)
        self.assertEqual(last_Two_Digits(99), 9)

    def test_edge_cases(self):
        self.assertEqual(last_Two_Digits(0), 0)
        self.assertEqual(last_Two_Digits(10), 1)
        self.assertEqual(last_Two_Digits(98), 8)
        self.assertEqual(last_Two_Digits(999), 9)

    def test_invalid_input(self):
        self.assertRaises(ValueError, last_Two_Digits, -1)
        self.assertRaises(ValueError, last_Two_Digits, 100)
