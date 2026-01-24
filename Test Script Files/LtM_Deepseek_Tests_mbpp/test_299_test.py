import unittest
from mbpp_299_code import max_aggregate

class TestMaxAggregate(unittest.TestCase):

    def test_simple_inputs(self):
        stdata = [('Alice', 85), ('Bob', 90), ('Charlie', 78)]
        self.assertEqual(max_aggregate(stdata), ('Bob', 90))

    def test_edge_conditions(self):
        # Test with empty input
        self.assertEqual(max_aggregate([]), None)

        # Test with single student data
        stdata = [('Eve', 95)]
        self.assertEqual(max_aggregate(stdata), ('Eve', 95))

    def test_boundary_conditions(self):
        # Test with maximum marks
        stdata = [('Max', 100), ('Min', 0)]
        self.assertEqual(max_aggregate(stdata), ('Max', 100))

        # Test with negative marks
        stdata = [('Neg', -50), ('Pos', 50)]
        self.assertEqual(max_aggregate(stdata), ('Pos', 50))

    def test_complex_cases(self):
        # Test with same marks
        stdata = [('Same1', 80), ('Same2', 80), ('Same3', 80)]
        self.assertEqual(max_aggregate(stdata), ('Same1', 80))

        # Test with mix of marks
        stdata = [('Mix1', 70), ('Mix2', 90), ('Mix3', 80)]
        self.assertEqual(max_aggregate(stdata), ('Mix2', 90))
