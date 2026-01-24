import unittest
from mbpp_555_code import difference

class TestDifference(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(difference(5), 110)

    def test_boundary_case(self):
        self.assertEqual(difference(1), 1)

    def test_edge_case(self):
        self.assertEqual(difference(0), 0)

    def test_negative_input(self):
        with self.assertRaises(Exception):
            difference(-1)
