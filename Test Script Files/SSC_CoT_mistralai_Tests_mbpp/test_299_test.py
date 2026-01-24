import unittest
from mbpp_299_code import defaultdict
from 299_code import max_aggregate

class TestMaxAggregate(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(max_aggregate([('Alice', 89), ('Bob', 75), ('Charlie', 94)]), ('Charlie', 94))
        self.assertEqual(max_aggregate([('Alice', 90), ('Bob', 80), ('Charlie', 85)]), ('Alice', 90))

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(max_aggregate([('Alice', 0), ('Bob', 0)]), ('Alice', 0))
        self.assertEqual(max_aggregate([('Alice', 100), ('Bob', 100)]), ('Alice', 100))
        self.assertEqual(max_aggregate([('Alice', -1), ('Bob', 0)]), ('Alice', -1))
        self.assertEqual(max_aggregate([('Alice', 1), ('Bob', 2), ('Charlie', 3), ('Dave', 4)]), ('Dave', 4))

    def test_multiple_max_values(self):
        self.assertEqual(max_aggregate([('Alice', 90), ('Bob', 90), ('Charlie', 85)]), ('Alice', 90))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_aggregate(123)
        with self.assertRaises(TypeError):
            max_aggregate([('Alice', 89), ('Bob', 75), ('Charlie', 94), {'name': 'Dave', 'marks': 88}])
