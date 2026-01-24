import unittest
from mbpp_360_code import get_carol

class TestGetCarol(unittest.TestCase):
    def test_get_carol_typical(self):
        self.assertEqual(get_carol(3), 35)

    def test_get_carol_edge(self):
        self.assertEqual(get_carol(0), -1)
        self.assertEqual(get_carol(1), -1)

    def test_get_carol_negative(self):
        with self.assertRaises(TypeError):
            get_carol(-1)

    def test_get_carol_large(self):
        self.assertEqual(get_carol(10), 18446744073709551615)

    def test_get_carol_zero(self):
        self.assertEqual(get_carol(0), -1)
