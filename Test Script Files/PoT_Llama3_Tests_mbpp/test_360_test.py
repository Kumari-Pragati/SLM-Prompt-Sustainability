import unittest
from mbpp_360_code import get_carol

class TestGetCarol(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_carol(1), 0)

    def test_edge_case(self):
        self.assertEqual(get_carol(0), 0)

    def test_edge_case2(self):
        self.assertEqual(get_carol(-1), -1)

    def test_edge_case3(self):
        self.assertEqual(get_carol(2), 3)

    def test_edge_case4(self):
        self.assertEqual(get_carol(3), 35)

    def test_edge_case5(self):
        self.assertEqual(get_carol(4), 257)

    def test_edge_case6(self):
        self.assertEqual(get_carol(5), 65537)

    def test_edge_case7(self):
        self.assertEqual(get_carol(6), 131071)

    def test_edge_case8(self):
        self.assertEqual(get_carol(7), 268435455)

    def test_edge_case9(self):
        self.assertEqual(get_carol(8), 4294967295)

    def test_edge_case10(self):
        self.assertEqual(get_carol(9), 18446744073709551615)
