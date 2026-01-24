import unittest
from mbpp_158_code import min_Ops

class TestMinOps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 2), 2)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 3), 1)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 4), 0)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 5), 0)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 6), -1)

    def test_edge_case_1(self):
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 1, 2), 4)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 1, 3), 3)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 1, 4), 2)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 1, 5), 1)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 1, 6), -1)

    def test_edge_case_2(self):
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 1), 0)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 4, 1), -1)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 3, 1), -1)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 2, 1), -1)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 1, 1), -1)

    def test_invalid_input(self):
        self.assertEqual(min_Ops([], 5, 2), -1)
        self.assertEqual(min_Ops([1], 5, 2), -1)
        self.assertEqual(min_Ops([1, 2], 0, 2), -1)
        self.assertEqual(min_Ops([1, 2, 3], 5, 0), -1)
        self.assertEqual(min_Ops([1, 2, 3], 5, -1), -1)
