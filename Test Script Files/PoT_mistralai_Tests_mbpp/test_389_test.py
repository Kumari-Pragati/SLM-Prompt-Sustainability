import unittest
from mbpp_389_code import find_lucas

class TestFindLucas(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(find_lucas(0), 2)
        self.assertEqual(find_lucas(1), 1)
        self.assertEqual(find_lucas(2), 3)
        self.assertEqual(find_lucas(3), 4)
        self.assertEqual(find_lucas(4), 7)
        self.assertEqual(find_lucas(5), 11)
        self.assertEqual(find_lucas(6), 18)
        self.assertEqual(find_lucas(7), 29)
        self.assertEqual(find_lucas(8), 47)
        self.assertEqual(find_lucas(9), 76)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(find_lucas(-1), None)
        self.assertEqual(find_lucas(10), 199)
        self.assertEqual(find_lucas(20), 3177)
        self.assertEqual(find_lucas(30), 514229)
        self.assertEqual(find_lucas(40), 8464479)
        self.assertEqual(find_lucas(50), 13958386244)
