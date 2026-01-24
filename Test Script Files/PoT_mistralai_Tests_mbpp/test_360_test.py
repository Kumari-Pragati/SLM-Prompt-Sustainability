import unittest
from mbpp_360_code import get_carol

class TestGetCarol(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(get_carol(0), 3)
        self.assertEqual(get_carol(1), 15)
        self.assertEqual(get_carol(2), 105)
        self.assertEqual(get_carol(3), 631)
        self.assertEqual(get_carol(4), 3875)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(get_carol(-1), -2)
        self.assertEqual(get_carol(50), 301002495)
        self.assertEqual(get_carol(0.5), -2)
        self.assertEqual(get_carol(1.5), -2)
