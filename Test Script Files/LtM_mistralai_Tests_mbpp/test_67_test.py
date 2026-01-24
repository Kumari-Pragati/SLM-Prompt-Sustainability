import unittest
from mbpp_67_code import bell_number

class TestBellNumber(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(bell_number(0), 1)
        self.assertEqual(bell_number(1), 1)
        self.assertEqual(bell_number(2), 2)
        self.assertEqual(bell_number(3), 4)
        self.assertEqual(bell_number(4), 10)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(bell_number(-1), None)
        self.assertEqual(bell_number(50), 1377056)
        self.assertEqual(bell_number(100), 3527187003)
