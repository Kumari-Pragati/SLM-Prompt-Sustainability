import unittest
from mbpp_608_code import bell_Number

class TestBellNumber(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(bell_Number(5), 52)

    def test_edge_condition(self):
        self.assertEqual(bell_Number(0), 1)

    def test_boundary_condition(self):
        self.assertEqual(bell_Number(1), 2)
        self.assertEqual(bell_Number(2), 5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            bell_Number('a')
        with self.assertRaises(ValueError):
            bell_Number(-1)
