import unittest
from mbpp_435_code import last_Digit

class TestLastDigit(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(last_Digit(123), 3)
        self.assertEqual(last_Digit(456), 6)
        self.assertEqual(last_Digit(789), 9)

    def test_edge_cases(self):
        self.assertEqual(last_Digit(0), 0)
        self.assertEqual(last_Digit(-10), 0)
        self.assertEqual(last_Digit(1000), 0)

    def test_negative_numbers(self):
        self.assertEqual(last_Digit(-123), 3)
        self.assertEqual(last_Digit(-456), 6)
        self.assertEqual(last_Digit(-789), 9)

    def test_zero(self):
        self.assertEqual(last_Digit(0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            last_Digit("abc")
