import unittest
from mbpp_608_code import bell_Number

class TestBellNumber(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(bell_Number(3), 2)

    def test_edge_case(self):
        self.assertEqual(bell_Number(1), 1)
        self.assertEqual(bell_Number(2), 2)

    def test_large_input(self):
        self.assertEqual(bell_Number(5), 5)

    def test_negative_input(self):
        with self.assertRaises(IndexError):
            bell_Number(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            bell_Number('a')

    def test_zero_input(self):
        self.assertEqual(bell_Number(0), 1)
