import unittest
from mbpp_555_code import difference

class TestDifference(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(difference(1), 1)
        self.assertEqual(difference(2), 5)
        self.assertEqual(difference(3), 14)
        self.assertEqual(difference(4), 30)

    def test_edge_cases(self):
        self.assertEqual(difference(0), 0)
        self.assertEqual(difference(-1), 0)

    def test_boundary_cases(self):
        self.assertEqual(difference(100), 500500)
        self.assertEqual(difference(200), 200200500)
