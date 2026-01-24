import unittest
from mbpp_299_code import max_aggregate

class TestMaxAggregate(unittest.TestCase):
    def test_max_aggregate_typical(self):
        stdata = [('Alice', 10), ('Bob', 20), ('Charlie', 30)]
        self.assertEqual(max_aggregate(stdata), ('Charlie', 30))

    def test_max_aggregate_edge(self):
        stdata = [('Alice', 10), ('Bob', 10), ('Charlie', 10)]
        self.assertEqual(max_aggregate(stdata), ('Alice', 10), ('Bob', 10), ('Charlie', 10))

    def test_max_aggregate_empty(self):
        stdata = []
        self.assertRaises(ZeroDivisionError, max_aggregate, stdata)

    def test_max_aggregate_single(self):
        stdata = [('Alice', 10)]
        self.assertEqual(max_aggregate(stdata), ('Alice', 10))

    def test_max_aggregate_multiple_max(self):
        stdata = [('Alice', 10), ('Bob', 10), ('Charlie', 10)]
        self.assertEqual(max_aggregate(stdata), ('Alice', 10), ('Bob', 10), ('Charlie', 10))
