import unittest
from mbpp_299_code import max_aggregate

class TestMaxAggregate(unittest.TestCase):
    def test_typical_input(self):
        stdata = [('Alice', 90), ('Bob', 80), ('Charlie', 70)]
        self.assertEqual(max_aggregate(stdata), ('Charlie', 70))

    def test_edge_case(self):
        stdata = [('Alice', 100), ('Bob', 100), ('Charlie', 100)]
        self.assertEqual(max_aggregate(stdata), ('Alice', 100))

    def test_boundary_case(self):
        stdata = [('Alice', 99), ('Bob', 100), ('Charlie', 98)]
        self.assertEqual(max_aggregate(stdata), ('Bob', 100))

    def test_multiple_max(self):
        stdata = [('Alice', 90), ('Bob', 90), ('Charlie', 90)]
        self.assertEqual(max_aggregate(stdata), max([('Alice', 90), ('Bob', 90), ('Charlie', 90)], key=lambda x: x[1]))

    def test_empty_input(self):
        stdata = []
        self.assertEqual(max_aggregate(stdata), ())

    def test_single_input(self):
        stdata = [('Alice', 90)]
        self.assertEqual(max_aggregate(stdata), ('Alice', 90))

    def test_invalid_input(self):
        stdata = ['Alice', 90]
        with self.assertRaises(TypeError):
            max_aggregate(stdata)
