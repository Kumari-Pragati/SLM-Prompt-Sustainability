import unittest
from mbpp_360_code import get_carol

class TestGetCarol(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(get_carol(0), 0)
        self.assertEqual(get_carol(1), 3)
        self.assertEqual(get_carol(2), 15)

    def test_edge_and_boundary(self):
        self.assertEqual(get_carol(-1), -2)
        self.assertEqual(get_carol(32), 4294967281)

    def test_complex_input(self):
        self.assertEqual(get_carol(10), 102320061)
        self.assertEqual(get_carol(30), 1073741823)
        self.assertEqual(get_carol(31), -2)
