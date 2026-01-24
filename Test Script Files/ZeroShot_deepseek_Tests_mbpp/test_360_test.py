import unittest
from mbpp_360_code import get_carol

class TestGetCarol(unittest.TestCase):

    def test_get_carol_positive(self):
        self.assertEqual(get_carol(1), 1)
        self.assertEqual(get_carol(2), 14)
        self.assertEqual(get_carol(3), 94)
        self.assertEqual(get_carol(4), 646)

    def test_get_carol_negative(self):
        self.assertEqual(get_carol(-1), -3)
        self.assertEqual(get_carol(-2), -14)
        self.assertEqual(get_carol(-3), -94)
        self.assertEqual(get_carol(-4), -646)

    def test_get_carol_zero(self):
        self.assertEqual(get_carol(0), 0)
