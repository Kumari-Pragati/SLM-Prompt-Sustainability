import unittest

from mbpp_692_code import last_Two_Digits

class TestLastTwoDigits(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(last_Two_Digits(5), 120)

    def test_boundary_case(self):
        self.assertEqual(last_Two_Digits(10), None)

    def test_edge_case(self):
        self.assertEqual(last_Two_Digits(0), 1)
        self.assertEqual(last_Two_Digits(1), 1)
        self.assertEqual(last_Two_Digits(2), 2)
        self.assertEqual(last_Two_Digits(3), 6)
        self.assertEqual(last_Two_Digits(4), 24)
        self.assertEqual(last_Two_Digits(5), 120)
        self.assertEqual(last_Two_Digits(6), 720)
        self.assertEqual(last_Two_Digits(7), 5040)
        self.assertEqual(last_Two_Digits(8), 40320)
        self.assertEqual(last_Two_Digits(9), 362880)
        self.assertEqual(last_Two_Digits(10), None)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            last_Two_Digits("1")
        with self.assertRaises(TypeError):
            last_Two_Digits(None)
        with self.assertRaises(TypeError):
            last_Two_Digits([1, 2, 3])
