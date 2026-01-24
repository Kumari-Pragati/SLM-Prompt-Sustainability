import unittest
from mbpp_692_code import last_Two_Digits

class TestLastTwoDigits(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(last_Two_Digits(5), 120)

    def test_boundary_conditions(self):
        self.assertEqual(last_Two_Digits(0), 1)
        self.assertEqual(last_Two_Digits(10), None)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            last_Two_Digits('a')
        with self.assertRaises(ValueError):
            last_Two_Digits(-5)
