import unittest
from mbpp_608_code import bell_Number

class TestBellNumber(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(bell_Number(3), 4)
        self.assertEqual(bell_Number(4), 10)
        self.assertEqual(bell_Number(5), 20)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(bell_Number(0), 1)
        self.assertEqual(bell_Number(1), 1)
        self.assertEqual(bell_Number(2), 2)
        self.assertEqual(bell_Number(100), 3542248481792619150)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            bell_Number(-1)
        with self.assertRaises(ValueError):
            bell_Number(float('nan'))
