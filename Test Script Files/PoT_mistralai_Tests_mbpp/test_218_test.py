import unittest
from mbpp_218_code import min_Operations

class TestMinOperations(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_Operations(10, 20), 9)
        self.assertEqual(min_Operations(20, 10), 9)
        self.assertEqual(min_Operations(2, 4), 1)
        self.assertEqual(min_Operations(4, 2), 1)

    def test_edge_cases(self):
        self.assertEqual(min_Operations(1, 1), 0)
        self.assertEqual(min_Operations(0, 1), 0)
        self.assertEqual(min_Operations(1, 0), math.inf)

    def test_boundary_cases(self):
        self.assertEqual(min_Operations(1, 2), 1)
        self.assertEqual(min_Operations(2, 1), 1)
        self.assertEqual(min_Operations(1, 0), math.inf)
        self.assertEqual(min_Operations(0, 1), 0)
