import unittest
from mbpp_67_code import bell_number

class TestBellNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(bell_number(1), 1)
        self.assertEqual(bell_number(2), 2)
        self.assertEqual(bell_number(3), 5)
        self.assertEqual(bell_number(4), 15)
        self.assertEqual(bell_number(5), 52)

    def test_boundary_conditions(self):
        self.assertEqual(bell_number(0), 1)

    def test_edge_cases(self):
        self.assertEqual(bell_number(6), 203)
        self.assertEqual(bell_number(7), 770)
        self.assertEqual(bell_number(8), 3432)
        self.assertEqual(bell_number(9), 16384)
        self.assertEqual(bell_number(10), 83779)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            bell_number('a')
        with self.assertRaises(ValueError):
            bell_number(-1)
