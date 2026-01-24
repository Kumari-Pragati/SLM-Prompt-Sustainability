import unittest
from mbpp_692_code import last_Two_Digits

class TestLastTwoDigits(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(last_Two_Digits(5), 120)

    def test_boundary_conditions(self):
        self.assertEqual(last_Two_Digits(0), 1)
        self.assertEqual(last_Two_Digits(10), None)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, last_Two_Digits, 'a')
        self.assertRaises(TypeError, last_Two_Digits, None)
        self.assertRaises(TypeError, last_Two_Digits, [1, 2, 3])
        self.assertRaises(TypeError, last_Two_Digits, {'a': 1, 'b': 2})
