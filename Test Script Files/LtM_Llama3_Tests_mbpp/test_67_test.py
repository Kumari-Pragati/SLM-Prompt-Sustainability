import unittest
from mbpp_67_code import bell_number

class TestBellNumber(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(bell_number(0), 1)
        self.assertEqual(bell_number(1), 1)
        self.assertEqual(bell_number(2), 2)
        self.assertEqual(bell_number(3), 5)
        self.assertEqual(bell_number(4), 29)

    def test_edge(self):
        self.assertEqual(bell_number(-1), None)
        self.assertEqual(bell_number(0.5), None)
        self.assertEqual(bell_number("a"), None)

    def test_large(self):
        self.assertEqual(bell_number(10), 99220)
        self.assertEqual(bell_number(20), 1125899906842624)
