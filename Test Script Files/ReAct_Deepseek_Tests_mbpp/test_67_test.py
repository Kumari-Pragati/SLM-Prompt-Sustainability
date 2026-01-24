import unittest
from mbpp_67_code import bell_number

class TestBellNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(bell_number(0), 1)
        self.assertEqual(bell_number(1), 1)
        self.assertEqual(bell_number(2), 2)
        self.assertEqual(bell_number(3), 5)
        self.assertEqual(bell_number(4), 15)

    def test_edge_cases(self):
        self.assertEqual(bell_number(0), 1)
        self.assertEqual(bell_number(1), 1)
        self.assertEqual(bell_number(2), 2)
        self.assertEqual(bell_number(3), 5)
        self.assertEqual(bell_number(4), 15)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            bell_number("5")
        with self.assertRaises(ValueError):
            bell_number(-1)
