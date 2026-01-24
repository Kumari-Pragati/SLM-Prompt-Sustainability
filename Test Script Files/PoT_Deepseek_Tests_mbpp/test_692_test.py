import unittest
from mbpp_692_code import last_Two_Digits

class TestLastTwoDigits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(last_Two_Digits(1), 1)
        self.assertEqual(last_Two_Digits(2), 2)
        self.assertEqual(last_Two_Digits(3), 6)
        self.assertEqual(last_Two_Digits(4), 24)
        self.assertEqual(last_Two_Digits(5), 120)

    def test_edge_cases(self):
        self.assertEqual(last_Two_Digits(0), 1)
        self.assertEqual(last_Two_Digits(10), 3628800)

    def test_boundary_conditions(self):
        self.assertEqual(last_Two_Digits(11), None)
        self.assertEqual(last_Two_Digits(-1), None)
        self.assertEqual(last_Two_Digits(100), None)
