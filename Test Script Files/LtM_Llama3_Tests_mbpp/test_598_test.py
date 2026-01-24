import unittest
from mbpp_598_code import armstrong_number

class TestArmstrongNumber(unittest.TestCase):
    def test_armstrong_number_simple(self):
        self.assertTrue(armstrong_number(153))
        self.assertTrue(armstrong_number(370371))
        self.assertFalse(armstrong_number(123))
        self.assertFalse(armstrong_number(12345))

    def test_armstrong_number_edge(self):
        self.assertFalse(armstrong_number(0))
        self.assertFalse(armstrong_number(1))
        self.assertFalse(armstrong_number(-1))
        self.assertFalse(armstrong_number(-123))

    def test_armstrong_number_invalid(self):
        with self.assertRaises(TypeError):
            armstrong_number("123")
        with self.assertRaises(TypeError):
            armstrong_number(None)
