import unittest
from mbpp_598_code import armstrong_number

class TestArmstrongNumber(unittest.TestCase):

    def test_simple_armstrong(self):
        self.assertTrue(armstrong_number(153))
        self.assertTrue(armstrong_number(370))
        self.assertTrue(armstrong_number(371))

    def test_edge_cases(self):
        self.assertFalse(armstrong_number(0))
        self.assertFalse(armstrong_number(1))
        self.assertFalse(armstrong_number(2))
        self.assertFalse(armstrong_number(3))
        self.assertFalse(armstrong_number(4))
        self.assertFalse(armstrong_number(5))
        self.assertFalse(armstrong_number(6))
        self.assertFalse(armstrong_number(7))
        self.assertFalse(armstrong_number(8))
        self.assertFalse(armstrong_number(9))
        self.assertTrue(armstrong_number(153 * 10 ** len(str(153))))
        self.assertTrue(armstrong_number(370 * 10 ** len(str(370))))
        self.assertTrue(armstrong_number(371 * 10 ** len(str(371))))

    def test_complex_cases(self):
        self.assertFalse(armstrong_number(123456789))
        self.assertFalse(armstrong_number(1234567890))
        self.assertFalse(armstrong_number(12345678901))
        self.assertFalse(armstrong_number(123456789012))
        self.assertFalse(armstrong_number(1234567890123))
        self.assertFalse(armstrong_number(12345678901234))
        self.assertFalse(armstrong_number(123456789012345))
        self.assertFalse(armstrong_number(1234567890123456))
        self.assertFalse(armstrong_number(12345678901234567))
        self.assertFalse(armstrong_number(123456789012345678))
        self.assertFalse(armstrong_number(1234567890123456789))
