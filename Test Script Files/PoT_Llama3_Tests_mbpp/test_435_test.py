import unittest
from mbpp_435_code import last_Digit

class TestLastDigit(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(last_Digit(123), 3)
        self.assertEqual(last_Digit(456), 6)
        self.assertEqual(last_Digit(789), 9)

    def test_edge(self):
        self.assertEqual(last_Digit(10), 0)
        self.assertEqual(last_Digit(20), 0)
        self.assertEqual(last_Digit(30), 0)

    def test_negative(self):
        self.assertEqual(last_Digit(-123), 3)
        self.assertEqual(last_Digit(-456), 6)
        self.assertEqual(last_Digit(-789), 9)

    def test_zero(self):
        self.assertEqual(last_Digit(0), 0)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            last_Digit("123")
