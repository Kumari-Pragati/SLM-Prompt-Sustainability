import unittest
from mbpp_365_code import count_Digit

class TestCountDigit(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Digit(12345), 5)
        self.assertEqual(count_Digit(987654321), 9)

    def test_edge_cases(self):
        self.assertEqual(count_Digit(0), 1)

    def test_corner_cases(self):
        self.assertEqual(count_Digit(10), 2)
        self.assertEqual(count_Digit(100), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Digit('12345')
        with self.assertRaises(TypeError):
            count_Digit(None)
