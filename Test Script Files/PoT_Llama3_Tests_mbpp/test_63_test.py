import unittest
from mbpp_63_code import max_difference

class TestMaxDifference(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_difference([(1, 3), (2, 4), (5, 7)]), 2)

    def test_edge_case(self):
        self.assertEqual(max_difference([(1, 1), (2, 2)]), 0)

    def test_edge_case2(self):
        self.assertEqual(max_difference([(1, 3), (3, 1)]), 2)

    def test_edge_case3(self):
        self.assertEqual(max_difference([(1, 2), (2, 1)]), 1)

    def test_edge_case4(self):
        self.assertEqual(max_difference([(1, 1), (1, 1)]), 0)

    def test_edge_case5(self):
        self.assertEqual(max_difference([]), None)

    def test_edge_case6(self):
        self.assertEqual(max_difference([(1, 1)]), 0)

    def test_edge_case7(self):
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4)]), 1)
