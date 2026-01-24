import unittest
from mbpp_608_code import bell_Number

class TestBellNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(bell_Number(1), 1)
        self.assertEqual(bell_Number(2), 2)
        self.assertEqual(bell_Number(3), 5)
        self.assertEqual(bell_Number(4), 15)
        self.assertEqual(bell_Number(5), 52)

    def test_boundary_conditions(self):
        self.assertEqual(bell_Number(0), 1)

    def test_edge_cases(self):
        self.assertEqual(bell_Number(6), 203)
        self.assertEqual(bell_Number(7), 770)
        self.assertEqual(bell_Number(8), 3329)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            bell_Number('a')
        with self.assertRaises(ValueError):
            bell_Number(-1)
