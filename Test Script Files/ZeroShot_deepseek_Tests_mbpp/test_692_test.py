import unittest
from mbpp_692_code import last_Two_Digits

class TestLastTwoDigits(unittest.TestCase):

    def test_last_Two_Digits(self):
        self.assertEqual(last_Two_Digits(10), 36)
        self.assertEqual(last_Two_Digits(15), 0)
        self.assertEqual(last_Two_Digits(20), 0)
        self.assertEqual(last_Two_Digits(25), 0)
        self.assertEqual(last_Two_Digits(30), 0)
        self.assertEqual(last_Two_Digits(35), 0)
        self.assertEqual(last_Two_Digits(40), 0)
        self.assertEqual(last_Two_Digits(45), 0)
        self.assertEqual(last_Two_Digits(50), 0)
        self.assertEqual(last_Two_Digits(55), 0)
        self.assertEqual(last_Two_Digits(60), 0)
        self.assertEqual(last_Two_Digits(65), 0)
        self.assertEqual(last_Two_Digits(70), 0)
        self.assertEqual(last_Two_Digits(75), 0)
        self.assertEqual(last_Two_Digits(80), 0)
        self.assertEqual(last_Two_Digits(85), 0)
        self.assertEqual(last_Two_Digits(90), 0)
        self.assertEqual(last_Two_Digits(95), 0)
        self.assertEqual(last_Two_Digits(100), 0)
