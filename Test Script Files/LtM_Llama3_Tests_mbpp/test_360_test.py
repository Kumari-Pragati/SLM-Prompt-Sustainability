import unittest
from mbpp_360_code import get_carol

class TestGetCarol(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(get_carol(0), -1)
        self.assertEqual(get_carol(1), -1)
        self.assertEqual(get_carol(2), 3)

    def test_edge(self):
        self.assertEqual(get_carol(-1), -1)
        self.assertEqual(get_carol(3), 11)

    def test_edge2(self):
        self.assertEqual(get_carol(4), 17)

    def test_edge3(self):
        self.assertEqual(get_carol(5), 29)

    def test_edge4(self):
        self.assertEqual(get_carol(6), 41)

    def test_edge5(self):
        self.assertEqual(get_carol(7), 53)

    def test_edge6(self):
        self.assertEqual(get_carol(8), 65)

    def test_edge7(self):
        self.assertEqual(get_carol(9), 77)

    def test_edge8(self):
        self.assertEqual(get_carol(10), 89)

    def test_edge9(self):
        self.assertEqual(get_carol(11), 101)

    def test_edge10(self):
        self.assertEqual(get_carol(12), 113)
