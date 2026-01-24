import unittest
from mbpp_299_code import max_aggregate

class TestMaxAggregate(unittest.TestCase):

    def test_typical_case(self):
        stdata = [('Alice', 90), ('Bob', 80), ('Charlie', 70)]
        self.assertEqual(max_aggregate(stdata), ('Charlie', 70))

    def test_edge_case(self):
        stdata = [('Alice', 100), ('Bob', 100), ('Charlie', 100)]
        self.assertEqual(max_aggregate(stdata), ('Alice', 100))

    def test_edge_case2(self):
        stdata = [('Alice', 0), ('Bob', 0), ('Charlie', 0)]
        self.assertEqual(max_aggregate(stdata), ('Alice', 0))

    def test_multiple_max(self):
        stdata = [('Alice', 90), ('Bob', 90), ('Charlie', 90)]
        self.assertEqual(max_aggregate(stdata), max([('Alice', 90), ('Bob', 90), ('Charlie', 90)], key=lambda x: x[1]))

    def test_empty_input(self):
        stdata = []
        self.assertRaises(TypeError, max_aggregate, stdata)

    def test_non_iterable_input(self):
        stdata = 'not a list'
        self.assertRaises(TypeError, max_aggregate, stdata)
