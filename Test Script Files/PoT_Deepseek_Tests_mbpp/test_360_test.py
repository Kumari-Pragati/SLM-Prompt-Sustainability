import unittest
from mbpp_360_code import get_carol

class TestGetCarol(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_carol(1), 2)
        self.assertEqual(get_carol(2), 14)
        self.assertEqual(get_carol(3), 94)

    def test_edge_cases(self):
        self.assertEqual(get_carol(0), 1)

    def test_boundary_cases(self):
        self.assertEqual(get_carol(10), 1023)
        self.assertEqual(get_carol(20), 1048575)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_carol('a')
        with self.assertRaises(ValueError):
            get_carol(-1)
