import unittest
from mbpp_360_code import get_carol

class TestGetCarol(unittest.TestCase):

    def test_get_carol_positive(self):
        self.assertEqual(get_carol(1), 3)
        self.assertEqual(get_carol(2), 9)
        self.assertEqual(get_carol(3), 35)

    def test_get_carol_negative(self):
        with self.assertRaises(TypeError):
            get_carol(-1)

    def test_get_carol_zero(self):
        self.assertEqual(get_carol(0), 0)

    def test_get_carol_non_integer(self):
        with self.assertRaises(TypeError):
            get_carol(1.5)
