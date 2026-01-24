import unittest
from mbpp_389_code import find_lucas

class TestFindLucas(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(find_lucas(0), 2)
        self.assertEqual(find_lucas(1), 1)
        self.assertEqual(find_lucas(2), 3)
        self.assertEqual(find_lucas(3), 4)
        self.assertEqual(find_lucas(4), 7)

    def test_edge_cases(self):
        self.assertEqual(find_lucas(-1), 1)
        self.assertEqual(find_lucas(-2), 2)

    def test_boundary_cases(self):
        self.assertEqual(find_lucas(30), 1074)
