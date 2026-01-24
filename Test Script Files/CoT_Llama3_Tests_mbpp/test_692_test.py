import unittest
from mbpp_692_code import last_Two_Digits

class TestLastTwoDigits(unittest.TestCase):
    def test_last_two_digits(self):
        self.assertEqual(last_Two_Digits(10), 0)
        self.assertEqual(last_Two_Digits(15), 40)
        self.assertEqual(last_Two_Digits(20), 6)
        self.assertEqual(last_Two_Digits(25), 0)
        self.assertEqual(last_Two_Digits(30), 0)
        self.assertEqual(last_Two_Digits(1), 1)
        self.assertEqual(last_Two_Digits(2), 2)
        self.assertEqual(last_Two_Digits(3), 6)
        self.assertEqual(last_Two_Digits(4), 24)
        self.assertEqual(last_Two_Digits(5), 60)
        self.assertEqual(last_Two_Digits(6), 0)
        self.assertEqual(last_Two_Digits(7), 0)
        self.assertEqual(last_Two_Digits(8), 0)
        self.assertEqual(last_Two_Digits(9), 0)
        self.assertEqual(last_Two_Digits(0), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            last_Two_Digits(None)
        with self.assertRaises(TypeError):
            last_Two_Digits("a")
        with self.assertRaises(TypeError):
            last_Two_Digits(10.5)
