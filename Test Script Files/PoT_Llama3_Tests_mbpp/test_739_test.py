import unittest
from mbpp_739_code import find_Index

class TestFindIndex(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Index(1), 10)

    def test_edge_case(self):
        self.assertEqual(find_Index(0), 10)

    def test_edge_case2(self):
        self.assertEqual(find_Index(-1), 10)

    def test_edge_case3(self):
        self.assertEqual(find_Index(2), 100)

    def test_edge_case4(self):
        self.assertEqual(find_Index(-2), 100)

    def test_edge_case5(self):
        self.assertEqual(find_Index(3), 1000)

    def test_edge_case6(self):
        self.assertEqual(find_Index(-3), 1000)

    def test_edge_case7(self):
        self.assertEqual(find_Index(4), 10000)

    def test_edge_case8(self):
        self.assertEqual(find_Index(-4), 10000)

    def test_edge_case9(self):
        self.assertEqual(find_Index(5), 100000)

    def test_edge_case10(self):
        self.assertEqual(find_Index(-5), 100000)
