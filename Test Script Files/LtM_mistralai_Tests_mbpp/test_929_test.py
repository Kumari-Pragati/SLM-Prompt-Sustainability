import unittest
from mbpp_929_code import count_tuplex

class TestCountTuplex(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_tuplex([1, 2, 3, 1, 2], 1), 3)
        self.assertEqual(count_tuplex([], 1), 0)
        self.assertEqual(count_tuplex([1], 1), 1)
        self.assertEqual(count_tuplex([1, 1], 1), 2)

    def test_edge_and_boundary(self):
        self.assertEqual(count_tuplex([-1, 0, 1], 0), 1)
        self.assertEqual(count_tuplex([-1, 0, 1], 1), 2)
        self.assertEqual(count_tuplex([-1, 0, 1], -1), 0)
        self.assertEqual(count_tuplex([-1, 0, 1], 2), 0)

    def test_complex(self):
        self.assertEqual(count_tuplex([1, 2, 3, 2, 1], 2), 3)
        self.assertEqual(count_tuplex([1, 2, 3, 2, 1], 3), 1)
        self.assertEqual(count_tuplex([1, 2, 3, 2, 1], 4), 0)
