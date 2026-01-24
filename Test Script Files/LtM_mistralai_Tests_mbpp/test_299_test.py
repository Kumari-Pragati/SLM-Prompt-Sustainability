import unittest
from mbpp_299_code import defaultdict
from 299_code import max_aggregate

class TestMaxAggregate(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(max_aggregate([('Alice', 80), ('Bob', 90), ('Charlie', 70)]), ('Bob', 90))
        self.assertEqual(max_aggregate([('Alice', 80), ('Bob', 90), ('Charlie', 70), ('Dave', 60)]), ('Bob', 90))

    def test_edge_cases(self):
        self.assertEqual(max_aggregate([('Alice', 0), ('Bob', 1)]), ('Bob', 1))
        self.assertEqual(max_aggregate([('Alice', 100), ('Bob', 100)]), ('Alice', 100))
        self.assertEqual(max_aggregate([('Alice', 80), ('Bob', 80), ('Charlie', 70)]), ('Alice', 80))
        self.assertEqual(max_aggregate([('Alice', 80), ('Bob', 80), ('Charlie', 70), ('Dave', 81)]), ('Dave', 81))

    def test_complex(self):
        self.assertEqual(max_aggregate([('Alice', 80), ('Bob', 80), ('Charlie', 70), ('Dave', 60), ('Eve', 90), ('Frank', 80)]), ('Eve', 90))
        self.assertEqual(max_aggregate([('Alice', 80), ('Bob', 80), ('Charlie', 70), ('Dave', 60), ('Eve', 90), ('Frank', 80), ('Alice', 81)]), ('Alice', 81))
