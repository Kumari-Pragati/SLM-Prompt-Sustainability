import unittest
from mbpp_292_code import find

class TestFind(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(find(10, 2), 5)

    def test_edge(self):
        self.assertEqual(find(1, 1), 1)
        self.assertEqual(find(-1, 1), 0)
        self.assertEqual(find(0, 1), 0)

    def test_edge2(self):
        self.assertEqual(find(10, 0), 0)
        self.assertEqual(find(0, 0), 0)

    def test_edge3(self):
        self.assertRaises(ZeroDivisionError, find, 10, 0)
