import unittest
from mbpp_348_code import find_ways

class TestFindWays(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_ways(4), 1)

    def test_edge_case(self):
        self.assertEqual(find_ways(2), 1)

    def test_edge_case2(self):
        self.assertEqual(find_ways(6), 2)

    def test_edge_case3(self):
        self.assertEqual(find_ways(8), 6)

    def test_edge_case4(self):
        self.assertEqual(find_ways(10), 22)

    def test_edge_case5(self):
        self.assertEqual(find_ways(12), 66)

    def test_edge_case6(self):
        self.assertEqual(find_ways(14), 220)

    def test_edge_case7(self):
        self.assertEqual(find_ways(16), 792)

    def test_edge_case8(self):
        self.assertEqual(find_ways(18), 9240)

    def test_edge_case9(self):
        self.assertEqual(find_ways(20), 24310)

    def test_edge_case10(self):
        self.assertEqual(find_ways(22), 498960)
