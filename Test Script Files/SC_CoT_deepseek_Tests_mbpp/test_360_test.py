import unittest

from mbpp_360_code import get_carol

class TestGetCarol(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_carol(2), 14)

    def test_edge_case(self):
        self.assertEqual(get_carol(0), 0)

    def test_boundary_case(self):
        self.assertEqual(get_carol(1), 2)

    def test_large_input(self):
        self.assertGreater(get_carol(10), 10**18)

    def test_negative_input(self):
        with self.assertRaises(Exception):
            get_carol(-1)
