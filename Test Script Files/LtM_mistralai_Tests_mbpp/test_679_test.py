import unittest
from mbpp_679_code import dict

from access_key import access_key

class TestAccessKey(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(access_key(dict(a=1, b=2), 0), 1)
        self.assertEqual(access_key(dict(a=1, b=2), 1), 2)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(access_key(dict(), 0), None)
        self.assertEqual(access_key(dict(a=1), 2), None)
        self.assertEqual(access_key(dict(a=1), -1), None)
        self.assertEqual(access_key(dict(a=1), len(dict(a=1))), None)

    def test_complex_input(self):
        self.assertEqual(access_key(dict(a=1, b=2, c=[3, 4]), 2), 4)
        self.assertEqual(access_key(dict(a=1, b=2, c=[3, 4]), 'c'), [3, 4])
        self.assertEqual(access_key(dict(a=1, b=2, c=[3, 4]), 'd'), None)
