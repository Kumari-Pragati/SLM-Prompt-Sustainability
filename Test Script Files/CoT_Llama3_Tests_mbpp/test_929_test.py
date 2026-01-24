import unittest
from mbpp_929_code import count_tuplex

class TestCountTuplex(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(count_tuplex((1,2,3,4,5), 3), 1)

    def test_edge(self):
        self.assertEqual(count_tuplex((1,2,3,4,5), 1), 1)
        self.assertEqual(count_tuplex((1,2,3,4,5), 5), 1)

    def test_edge2(self):
        self.assertEqual(count_tuplex((1,2,3,4,5), 6), 0)

    def test_edge3(self):
        self.assertEqual(count_tuplex((1,2,3,4,5), 0), 0)

    def test_edge4(self):
        self.assertEqual(count_tuplex([], 1), 0)

    def test_edge5(self):
        self.assertEqual(count_tuplex([1], 1), 1)

    def test_edge6(self):
        self.assertEqual(count_tuplex([1,2,3,4,5], 1), 1)

    def test_edge7(self):
        self.assertEqual(count_tuplex([1,2,3,4,5], 2), 1)

    def test_edge8(self):
        self.assertEqual(count_tuplex([1,2,3,4,5], 3), 1)

    def test_edge9(self):
        self.assertEqual(count_tuplex([1,2,3,4,5], 4), 1)

    def test_edge10(self):
        self.assertEqual(count_tuplex([1,2,3,4,5], 5), 1)
