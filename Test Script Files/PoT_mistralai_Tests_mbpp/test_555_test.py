import unittest
from mbpp_555_code import difference

class TestDifference(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(difference(1), 0)
        self.assertEqual(difference(2), 1)
        self.assertEqual(difference(3), 6)
        self.assertEqual(difference(4), 10)
        self.assertEqual(difference(5), 15)

    def test_edge_cases(self):
        self.assertEqual(difference(0), 0)
        self.assertEqual(difference(100), 49950)

    def test_boundary_cases(self):
        self.assertEqual(difference(-1), -1)
        self.assertEqual(difference(100000), 50000000000)
