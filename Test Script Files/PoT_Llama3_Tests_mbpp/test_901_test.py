import unittest
from mbpp_901_code import smallest_multiple

class TestSmallestMultiple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(smallest_multiple(1), 1)
        self.assertEqual(smallest_multiple(2), 2)
        self.assertEqual(smallest_multiple(3), 6)
        self.assertEqual(smallest_multiple(4), 12)
        self.assertEqual(smallest_multiple(5), 60)

    def test_edge_case(self):
        self.assertEqual(smallest_multiple(6), 12)
        self.assertEqual(smallest_multiple(7), 84)
        self.assertEqual(smallest_multiple(8), 24)
        self.assertEqual(smallest_multiple(9), 18)
        self.assertEqual(smallest_multiple(10), 60)

    def test_boundary_case(self):
        self.assertEqual(smallest_multiple(11), 1326)
        self.assertEqual(smallest_multiple(12), 12)
        self.assertEqual(smallest_multiple(13), 5468)
        self.assertEqual(smallest_multiple(14), 1680)
        self.assertEqual(smallest_multiple(15), 3600)

    def test_corner_case(self):
        self.assertEqual(smallest_multiple(16), 1920)
        self.assertEqual(smallest_multiple(17), 28928)
        self.assertEqual(smallest_multiple(18), 4320)
        self.assertEqual(smallest_multiple(19), 11664)
        self.assertEqual(smallest_multiple(20), 14400)
