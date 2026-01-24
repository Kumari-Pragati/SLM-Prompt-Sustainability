import unittest
from mbpp_360_code import get_carol

class TestGetCarol(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(get_carol(0), 3)
        self.assertEqual(get_carol(1), 13)
        self.assertEqual(get_carol(2), 107)
        self.assertEqual(get_carol(3), 2039)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_carol(-1), -2)
        self.assertEqual(get_carol(42), 84157017)
        self.assertEqual(get_carol(0.5), -2)
        self.assertEqual(get_carol(float('inf')), -2)
        self.assertEqual(get_carol(float('nan')), float('nan'))
