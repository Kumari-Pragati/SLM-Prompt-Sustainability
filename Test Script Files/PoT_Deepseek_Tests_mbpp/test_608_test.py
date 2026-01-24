import unittest
from mbpp_608_code import bell_Number

class TestBellNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(bell_Number(1), 1)
        self.assertEqual(bell_Number(2), 2)
        self.assertEqual(bell_Number(3), 5)
        self.assertEqual(bell_Number(4), 15)

    def test_edge_cases(self):
        self.assertEqual(bell_Number(0), 0)

    def test_boundary_cases(self):
        self.assertEqual(bell_Number(10), 5040)
        self.assertEqual(bell_Number(20), 1307910)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            bell_Number('a')
        with self.assertRaises(ValueError):
            bell_Number(-1)
