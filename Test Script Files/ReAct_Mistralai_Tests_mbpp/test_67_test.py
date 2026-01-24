import unittest
from mbpp_67_code import bell_number

class TestBellNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(bell_number(1), 1)
        self.assertEqual(bell_number(2), 2)
        self.assertEqual(bell_number(3), 4)
        self.assertEqual(bell_number(4), 10)
        self.assertEqual(bell_number(5), 20)

    def test_edge_case_zero(self):
        self.assertEqual(bell_number(0), 1)

    def test_edge_case_negative(self):
        with self.assertRaises(ValueError):
            bell_number(-1)

    def test_edge_case_large_input(self):
        with self.assertRaises(ValueError):
            bell_number(1000)
