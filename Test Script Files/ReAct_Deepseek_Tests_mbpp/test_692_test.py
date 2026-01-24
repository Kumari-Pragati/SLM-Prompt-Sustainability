import unittest
from mbpp_692_code import last_Two_Digits

class TestLastTwoDigits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(last_Two_Digits(5), 120)
        self.assertEqual(last_Two_Digits(7), 5040)
        self.assertEqual(last_Two_Digits(10), 3628800)

    def test_boundary_cases(self):
        self.assertEqual(last_Two_Digits(0), 1)
        self.assertEqual(last_Two_Digits(1), 1)
        self.assertEqual(last_Two_Digits(2), 2)
        self.assertEqual(last_Two_Digits(9), 362880)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            last_Two_Digits('a')
        with self.assertRaises(ValueError):
            last_Two_Digits(-5)
