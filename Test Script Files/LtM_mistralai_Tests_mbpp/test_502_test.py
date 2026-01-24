import unittest
from mbpp_502_code import find

class TestFind(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find(5, 3), 2)
        self.assertEqual(find(10, 3), 1)
        self.assertEqual(find(15, 5), 0)

    def test_edge_cases(self):
        self.assertEqual(find(0, 3), 0)
        self.assertEqual(find(3, 3), 0)
        self.assertEqual(find(-5, 3), 1)

    def test_negative_m(self):
        self.assertEqual(find(5, -3), 2)
        self.assertEqual(find(-5, -3), 1)

    def test_divisible_by_m(self):
        self.assertEqual(find(6, 3), 0)
        self.assertEqual(find(-6, 3), 0)
