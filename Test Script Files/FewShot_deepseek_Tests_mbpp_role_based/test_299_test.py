import unittest
from mbpp_299_code import max_aggregate

class TestMaxAggregate(unittest.TestCase):
    def test_typical_use_case(self):
        stdata = [('Alice', 85), ('Bob', 90), ('Charlie', 75)]
        self.assertEqual(max_aggregate(stdata), ('Bob', 90))

    def test_edge_case_single_student(self):
        stdata = [('Eve', 95)]
        self.assertEqual(max_aggregate(stdata), ('Eve', 95))

    def test_boundary_case_same_max_marks(self):
        stdata = [('Frank', 80), ('Grace', 80), ('Helen', 70)]
        self.assertEqual(max_aggregate(stdata), ('Frank', 80))

    def test_invalid_input_empty_list(self):
        stdata = []
        self.assertRaises(ValueError, max_aggregate, stdata)

    def test_invalid_input_non_tuple(self):
        stdata = [('Ivan', 80), 'Bob', ('Charlie', 75)]
        self.assertRaises(TypeError, max_aggregate, stdata)
