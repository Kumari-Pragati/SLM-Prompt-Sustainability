import unittest
from mbpp_608_code import bell_Number

class TestBellNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(bell_Number(0), 1)
        self.assertEqual(bell_Number(1), 2)
        self.assertEqual(bell_Number(2), 5)
        self.assertEqual(bell_Number(3), 15)
        self.assertEqual(bell_Number(4), 52)

    def test_edge_cases(self):
        self.assertEqual(bell_Number(0), 1)
        self.assertEqual(bell_Number(10), 50129)
        self.assertEqual(bell_Number(20), 130798973051)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            bell_Number(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            bell_Number(1.5)

    def test_large_input(self):
        with self.assertRaises(RecursionError):
            bell_Number(1000)
