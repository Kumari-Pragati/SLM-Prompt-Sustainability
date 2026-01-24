import unittest
from mbpp_67_code import bell_number

class TestBellNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(bell_number(1), 1)
        self.assertEqual(bell_number(2), 2)
        self.assertEqual(bell_number(3), 5)
        self.assertEqual(bell_number(4), 15)
        self.assertEqual(bell_number(5), 52)

    def test_edge_cases(self):
        self.assertEqual(bell_number(0), 1)

    def test_boundary_cases(self):
        self.assertEqual(bell_number(10), 5012)
        self.assertEqual(bell_number(20), 1307915481)

    def test_invalid_input(self):
        with self.assertRaises(Exception):
            bell_number(-1)
        with self.assertRaises(Exception):
            bell_number(1.5)
        with self.assertRaises(Exception):
            bell_number('abc')
