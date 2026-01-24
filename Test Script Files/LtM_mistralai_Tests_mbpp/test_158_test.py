import unittest
from mbpp_158_code import min_Ops

class TestMinOps(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(min_Ops([1, 2, 3], 3, 1), 3)
        self.assertEqual(min_Ops([1, 2, 3], 3, 2), 2)
        self.assertEqual(min_Ops([1, 2, 3], 3, 3), 0)

    def test_edge_case(self):
        self.assertEqual(min_Ops([1, 2, 3], 3, 4), -1)
        self.assertEqual(min_Ops([1, 2, 3], 1, 1), 0)
        self.assertEqual(min_Ops([1, 2, 3], 2, 2), 1)

    def test_boundary_case(self):
        self.assertEqual(min_Ops([], 0, 1), 0)
        self.assertEqual(min_Ops([1], 1, 1), 0)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 1), 0)

    def test_complex_case(self):
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 3, 2), 5)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 4, 2), 4)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 2), 0)
