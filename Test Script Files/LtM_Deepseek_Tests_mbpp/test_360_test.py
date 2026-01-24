import unittest
from mbpp_360_code import get_carol

class TestGetCarol(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(get_carol(1), 2)
        self.assertEqual(get_carol(2), 14)

    def test_boundary_conditions(self):
        self.assertEqual(get_carol(0), 0)
        self.assertEqual(get_carol(10), 1022)

    def test_edge_cases(self):
        self.assertEqual(get_carol(-1), -2)
        self.assertEqual(get_carol(100), 1048574)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_carol('a')
        with self.assertRaises(ValueError):
            get_carol(-2)
