import unittest
from mbpp_299_code import max_aggregate

class TestMaxAggregate(unittest.TestCase):

    def test_typical_case(self):
        stdata = [('Alice', 85), ('Bob', 90), ('Charlie', 75)]
        self.assertEqual(max_aggregate(stdata), ('Bob', 90))

    def test_same_max_value(self):
        stdata = [('Alice', 85), ('Bob', 85), ('Charlie', 75)]
        self.assertEqual(max_aggregate(stdata), ('Alice', 85))

    def test_empty_data(self):
        stdata = []
        self.assertIsNone(max_aggregate(stdata))

    def test_single_student(self):
        stdata = [('Alice', 85)]
        self.assertEqual(max_aggregate(stdata), ('Alice', 85))

    def test_negative_marks(self):
        stdata = [('Alice', -5), ('Bob', 0), ('Charlie', 5)]
        self.assertEqual(max_aggregate(stdata), ('Charlie', 5))

    def test_zero_marks(self):
        stdata = [('Alice', 0), ('Bob', 0), ('Charlie', 0)]
        self.assertEqual(max_aggregate(stdata), ('Alice', 0))
