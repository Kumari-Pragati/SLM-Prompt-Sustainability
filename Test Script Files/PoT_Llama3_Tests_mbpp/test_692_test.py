import unittest
from mbpp_692_code import last_Two_Digits

class TestLastTwoDigits(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(last_Two_Digits(15), 15)

    def test_edge_case_zero(self):
        self.assertEqual(last_Two_Digits(0), 1)

    def test_edge_case_one(self):
        self.assertEqual(last_Two_Digits(1), 1)

    def test_edge_case_ten(self):
        self.assertEqual(last_Two_Digits(10), 3628800)

    def test_edge_case_large(self):
        self.assertEqual(last_Two_Digits(20), 2432902008176640000)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            last_Two_Digits(-1)

    def test_edge_case_non_integer(self):
        with self.assertRaises(TypeError):
            last_Two_Digits('a')
