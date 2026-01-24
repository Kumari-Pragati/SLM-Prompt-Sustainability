import unittest
from mbpp_970_code import min_of_two

class TestMinOfTwo(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_of_two(1, 2), 1)
        self.assertEqual(min_of_two(2, 1), 1)
        self.assertEqual(min_of_two(0, 1), 0)
        self.assertEqual(min_of_two(1, 0), 0)

    def test_edge_case(self):
        self.assertEqual(min_of_two(0, 0), 0)

    def test_boundary_case(self):
        self.assertEqual(min_of_two(-1, 0), -1)
        self.assertEqual(min_of_two(0, -1), -1)
        self.assertEqual(min_of_two(-1, -1), -1)
