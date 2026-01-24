import unittest
from mbpp_360_code import get_carol

class TestGetCarol(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(get_carol(2), 20)

    def test_boundary_condition(self):
        self.assertEqual(get_carol(1), 2)

    def test_edge_condition(self):
        self.assertEqual(get_carol(0), 0)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            get_carol(-1)
