import unittest
from mbpp_299_code import defaultdict
from mbpp_299_code import max_aggregate

class TestMaxAggregate(unittest.TestCase):

    def test_max_aggregate(self):
        stdata = [('Alice', 90), ('Bob', 85), ('Charlie', 95), ('Alice', 88)]
        expected_output = ('Charlie', 95)
        self.assertEqual(max_aggregate(stdata), expected_output)

    def test_max_aggregate_with_same_max_marks(self):
        stdata = [('Alice', 90), ('Bob', 90), ('Charlie', 95), ('Alice', 95)]
        expected_output = ('Alice', 95)
        self.assertEqual(max_aggregate(stdata), expected_output)

    def test_max_aggregate_with_empty_list(self):
        stdata = []
        expected_output = None
        self.assertEqual(max_aggregate(stdata), expected_output)

    def test_max_aggregate_with_single_student(self):
        stdata = [('Alice', 90)]
        expected_output = ('Alice', 90)
        self.assertEqual(max_aggregate(stdata), expected_output)
