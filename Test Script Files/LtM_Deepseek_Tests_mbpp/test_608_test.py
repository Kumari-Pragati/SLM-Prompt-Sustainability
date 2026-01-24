import unittest
from mbpp_608_code import bell_Number

class TestBellNumber(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(bell_Number(1), 1)
        self.assertEqual(bell_Number(2), 2)
        self.assertEqual(bell_Number(3), 5)

    def test_boundary_conditions(self):
        self.assertEqual(bell_Number(0), 1)

    def test_edge_conditions(self):
        self.assertEqual(bell_Number(4), 15)
        self.assertEqual(bell_Number(5), 52)

    def test_invalid_inputs(self):
        with self.assertRaises(Exception):
            bell_Number(-1)
        with self.assertRaises(Exception):
            bell_Number(1000)
