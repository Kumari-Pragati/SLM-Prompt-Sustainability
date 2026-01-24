import unittest
from mbpp_218_code import min_Operations

class TestMinOperations(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(min_Operations(4, 7), 2)
        self.assertEqual(min_Operations(7, 4), 2)
        self.assertEqual(min_Operations(2, 3), 1)
        self.assertEqual(min_Operations(3, 2), 1)

    def test_edge_and_boundary(self):
        self.assertEqual(min_Operations(1, 2), 0)
        self.assertEqual(min_Operations(2, 1), 0)
        self.assertEqual(min_Operations(1, 1), 0)
        self.assertEqual(min_Operations(math.inf, 2), math.inf - 1)
        self.assertEqual(min_Operations(2, math.inf), 1)

    def test_complex(self):
        self.assertEqual(min_Operations(5, 10), 3)
        self.assertEqual(min_Operations(10, 5), 3)
        self.assertEqual(min_Operations(15, 24), 8)
        self.assertEqual(min_Operations(24, 15), 8)
