import unittest
from mbpp_360_code import get_carol

class TestGetCarol(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_carol(2), 14)

    def test_zero_case(self):
        self.assertEqual(get_carol(0), 0)

    def test_negative_case(self):
        with self.assertRaises(Exception):
            get_carol(-1)

    def test_large_number_case(self):
        self.assertEqual(get_carol(10), 1048574)

    def test_max_integer_case(self):
        self.assertEqual(get_carol(1000), 107150860718626732094842504906000888625)
