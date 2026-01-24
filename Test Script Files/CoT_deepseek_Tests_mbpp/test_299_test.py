import unittest
from mbpp_299_code import max_aggregate

class TestMaxAggregate(unittest.TestCase):

    def test_typical_case(self):
        stdata = [('Alice', 85), ('Bob', 90), ('Charlie', 75)]
        self.assertEqual(max_aggregate(stdata), ('Bob', 90))

    def test_single_student(self):
        stdata = [('Alice', 85)]
        self.assertEqual(max_aggregate(stdata), ('Alice', 85))

    def test_empty_data(self):
        stdata = []
        self.assertIsNone(max_aggregate(stdata))

    def test_negative_marks(self):
        stdata = [('Alice', -5), ('Bob', 10)]
        self.assertEqual(max_aggregate(stdata), ('Bob', 10))

    def test_same_marks(self):
        stdata = [('Alice', 85), ('Bob', 85), ('Charlie', 85)]
        self.assertEqual(max_aggregate(stdata), ('Alice', 85))

    def test_invalid_input(self):
        stdata = [('Alice', 'invalid')]
        with self.assertRaises(TypeError):
            max_aggregate(stdata)
