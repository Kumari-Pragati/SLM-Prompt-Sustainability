import unittest
from mbpp_348_code import find_ways

class TestFindWays(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_ways(4), 1)

    def test_edge_case(self):
        self.assertEqual(find_ways(2), 0)

    def test_boundary_case(self):
        self.assertEqual(find_ways(0), 0)
        self.assertEqual(find_ways(1), 0)

    def test_special_case(self):
        self.assertEqual(find_ways(8), 28)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_ways("invalid")
        with self.assertRaises(ValueError):
            find_ways(-1)
