import unittest
from mbpp_555_code import difference

class TestDifference(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(difference(5), 110)

    def test_boundary_condition(self):
        self.assertEqual(difference(1), 1)

    def test_edge_condition(self):
        self.assertEqual(difference(0), 0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            difference(-1)
