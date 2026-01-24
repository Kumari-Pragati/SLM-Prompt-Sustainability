import unittest
from mbpp_692_code import last_Two_Digits

class TestLastTwoDigits(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(last_Two_Digits(10), 10)
        self.assertEqual(last_Two_Digits(20), 20)
        self.assertEqual(last_Two_Digits(30), 6)

    def test_edge_cases(self):
        self.assertEqual(last_Two_Digits(0), 1)
        self.assertEqual(last_Two_Digits(1), 1)
        self.assertEqual(last_Two_Digits(9), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            last_Two_Digits('a')
        with self.assertRaises(TypeError):
            last_Two_Digits(None)

    def test_large_inputs(self):
        self.assertEqual(last_Two_Digits(100), 40)
        self.assertEqual(last_Two_Digits(200), 24)
