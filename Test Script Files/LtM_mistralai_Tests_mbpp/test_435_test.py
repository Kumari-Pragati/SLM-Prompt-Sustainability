import unittest
from mbpp_435_code import last_Digit

class TestLastDigit(unittest.TestCase):
    def test_simple_positive(self):
        self.assertEqual(last_Digit(123), 3)
        self.assertEqual(last_Digit(987), 7)

    def test_simple_negative(self):
        self.assertEqual(last_Digit(-123), 3)
        self.assertEqual(last_Digit(-987), 7)

    def test_edge_cases(self):
        self.assertEqual(last_Digit(0), 0)
        self.assertEqual(last_Digit(10 ** 100), 0)

    def test_complex_cases(self):
        self.assertEqual(last_Digit(1024), 4)
        self.assertEqual(last_Digit(1023), 3)
        self.assertEqual(last_Digit(1022), 2)
        self.assertEqual(last_Digit(1021), 1)
        self.assertEqual(last_Digit(1020), 0)
