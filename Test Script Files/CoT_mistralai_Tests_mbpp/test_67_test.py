import unittest
from67_code import bell_number

class TestBellNumber(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(bell_number(0), 1)
        self.assertEqual(bell_number(1), 1)
        self.assertEqual(bell_number(2), 2)
        self.assertEqual(bell_number(3), 4)
        self.assertEqual(bell_number(4), 10)
        self.assertEqual(bell_number(5), 20)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(bell_number(-1), None)
        self.assertEqual(bell_number(6), 52)
        self.assertEqual(bell_number(7), 155)
        self.assertEqual(bell_number(8), 429)
        self.assertEqual(bell_number(9), 1131)
        self.assertEqual(bell_number(10), 3178)
