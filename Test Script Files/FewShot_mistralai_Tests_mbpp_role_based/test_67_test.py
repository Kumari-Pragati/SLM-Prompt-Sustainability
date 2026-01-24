import unittest
from mbpp_67_code import bell_number

class TestBellNumber(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(bell_number(3), 5)
        self.assertEqual(bell_number(4), 15)
        self.assertEqual(bell_number(5), 25)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(bell_number(0), 1)
        self.assertEqual(bell_number(1), 1)
        self.assertEqual(bell_number(2), 2)
        self.assertEqual(bell_number(6), 46)
        self.assertEqual(bell_number(7), 81)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            bell_number(-1)
        with self.assertRaises(ValueError):
            bell_number(float('nan'))
