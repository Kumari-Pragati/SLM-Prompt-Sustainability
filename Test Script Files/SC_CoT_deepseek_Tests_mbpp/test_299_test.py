import unittest
from mbpp_299_code import max_aggregate

class TestMaxAggregate(unittest.TestCase):

    def test_typical_case(self):
        stdata = [('Alice', 90), ('Bob', 85), ('Charlie', 95)]
        self.assertEqual(max_aggregate(stdata), ('Charlie', 95))

    def test_edge_case_single_student(self):
        stdata = [('Alice', 90)]
        self.assertEqual(max_aggregate(stdata), ('Alice', 90))

    def test_edge_case_same_max_marks(self):
        stdata = [('Alice', 90), ('Bob', 90), ('Charlie', 90)]
        self.assertIn(max_aggregate(stdata), [('Alice', 90), ('Bob', 90), ('Charlie', 90)])

    def test_invalid_input_empty_list(self):
        stdata = []
        with self.assertRaises(ValueError):
            max_aggregate(stdata)

    def test_invalid_input_non_tuple(self):
        stdata = [('Alice', 90), ('Bob', 85), 95]
        with self.assertRaises(TypeError):
            max_aggregate(stdata)
