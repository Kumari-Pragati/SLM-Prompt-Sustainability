import unittest
from mbpp_299_code import max_aggregate

class TestMaxAggregate(unittest.TestCase):

    def test_typical_case(self):
        stdata = [('Alice', 85), ('Bob', 90), ('Charlie', 80)]
        self.assertEqual(max_aggregate(stdata), ('Bob', 90))

    def test_edge_case_single_student(self):
        stdata = [('Eve', 95)]
        self.assertEqual(max_aggregate(stdata), ('Eve', 95))

    def test_boundary_case_same_max_marks(self):
        stdata = [('Frank', 80), ('Grace', 80), ('Helen', 75)]
        self.assertEqual(max_aggregate(stdata), ('Frank', 80))

    def test_corner_case_empty_data(self):
        stdata = []
        self.assertIsNone(max_aggregate(stdata))

    def test_corner_case_negative_marks(self):
        stdata = [('Ivan', -10), ('Judy', 20)]
        self.assertEqual(max_aggregate(stdata), ('Judy', 20))
