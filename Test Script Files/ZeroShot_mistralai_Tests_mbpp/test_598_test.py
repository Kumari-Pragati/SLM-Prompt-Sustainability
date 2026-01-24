import unittest
from mbpp_598_code import armstrong_number

class TestArmstrongNumber(unittest.TestCase):

    def test_armstrong_number_153(self):
        self.assertTrue(armstrong_number(153))

    def test_armstrong_number_370(self):
        self.assertTrue(armstrong_number(370))

    def test_armstrong_number_1634(self):
        self.assertTrue(armstrong_number(1634))

    def test_armstrong_number_1757(self):
        self.assertTrue(armstrong_number(1757))

    def test_armstrong_number_40785(self):
        self.assertTrue(armstrong_number(40785))

    def test_armstrong_number_16341(self):
        self.assertFalse(armstrong_number(16341))

    def test_armstrong_number_198(self):
        self.assertFalse(armstrong_number(198))

    def test_armstrong_number_951(self):
        self.assertFalse(armstrong_number(951))
