import unittest
from mbpp_765_code import is_polite

class TestIsPolite(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(is_polite(1), 2)

    def test_edge_case(self):
        self.assertEqual(is_polite(0), 1)

    def test_edge_case2(self):
        self.assertEqual(is_polite(-1), 0)

    def test_edge_case3(self):
        self.assertEqual(is_polite(-10), -9)

    def test_edge_case4(self):
        self.assertEqual(is_polite(10), 11)

    def test_edge_case5(self):
        self.assertEqual(is_polite(100), 101)

    def test_edge_case6(self):
        self.assertEqual(is_polite(-100), -99)

    def test_edge_case7(self):
        self.assertEqual(is_polite(0.5), 1)

    def test_edge_case8(self):
        self.assertEqual(is_polite(-0.5), 0)

    def test_edge_case9(self):
        self.assertEqual(is_polite(0.1), 1)

    def test_edge_case10(self):
        self.assertEqual(is_polite(-0.1), 0)
