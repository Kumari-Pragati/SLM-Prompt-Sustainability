import unittest
from mbpp_365_code import count_Digit

class TestCountDigit(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(count_Digit(0), 1)
        self.assertEqual(count_Digit(10), 2)
        self.assertEqual(count_Digit(123), 3)
        self.assertEqual(count_Digit(1000), 4)
        self.assertEqual(count_Digit(123456), 6)

    def test_edge_cases(self):
        self.assertEqual(count_Digit(-10), 2)
        self.assertEqual(count_Digit(-123), 3)
        self.assertEqual(count_Digit(0), 1)
        self.assertEqual(count_Digit(999999), 6)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Digit('abc')
        with self.assertRaises(TypeError):
            count_Digit(None)
