import unittest
from mbpp_692_code import last_Two_Digits

class TestLastTwoDigits(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(last_Two_Digits(15), 15)
        self.assertEqual(last_Two_Digits(25), 0)
        self.assertEqual(last_Two_Digits(35), 20)
        self.assertEqual(last_Two_Digits(45), 40)
        self.assertEqual(last_Two_Digits(55), 40)

    def test_edge_cases(self):
        self.assertEqual(last_Two_Digits(9), 0)
        self.assertEqual(last_Two_Digits(10), 3628800)
        self.assertEqual(last_Two_Digits(11), 3628800)
        self.assertEqual(last_Two_Digits(12), 3628800)

    def test_boundary_cases(self):
        self.assertEqual(last_Two_Digits(1), 1)
        self.assertEqual(last_Two_Digits(2), 2)
        self.assertEqual(last_Two_Digits(3), 6)
        self.assertEqual(last_Two_Digits(4), 24)
        self.assertEqual(last_Two_Digits(5), 60)
        self.assertEqual(last_Two_Digits(6), 60)
        self.assertEqual(last_Two_Digits(7), 840)
        self.assertEqual(last_Two_Digits(8), 40320)
        self.assertEqual(last_Two_Digits(9), 362880)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            last_Two_Digits('a')
        with self.assertRaises(TypeError):
            last_Two_Digits(None)
        with self.assertRaises(TypeError):
            last_Two_Digits('')
