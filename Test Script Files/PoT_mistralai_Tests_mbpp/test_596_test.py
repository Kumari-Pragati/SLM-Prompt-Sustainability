import unittest
from mbpp_596_code import tuple_size

class TestTupleSize(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(tuple_size(()), 24)
        self.assertEqual(tuple_size((1,)), 28)
        self.assertEqual(tuple_size((1, 2, 3)), 48)
        self.assertEqual(tuple_size((1, 2, 3, 4, 5)), 60)

    def test_edge_cases(self):
        self.assertEqual(tuple_size((sys.maxsize,)), 56)
        self.assertEqual(tuple_size((sys.maxsize, sys.maxsize)), 112)

    def test_corner_cases(self):
        self.assertEqual(tuple_size((tuple(),)), 40)
        self.assertEqual(tuple_size((frozenset(),)), 40)
        self.assertEqual(tuple_size((set(),)), 48)
        self.assertEqual(tuple_size((list(),)), 48)
