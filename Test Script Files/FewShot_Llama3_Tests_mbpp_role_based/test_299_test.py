import unittest
from mbpp_299_code import max_aggregate

class TestMaxAggregate(unittest.TestCase):
    def test_typical_use_case(self):
        stdata = [('Alice', 10), ('Bob', 20), ('Charlie', 30)]
        self.assertEqual(max_aggregate(stdata), ('Charlie', 30))

    def test_single_student(self):
        stdata = [('Alice', 10)]
        self.assertEqual(max_aggregate(stdata), ('Alice', 10))

    def test_multiple_students_with_same_marks(self):
        stdata = [('Alice', 10), ('Bob', 10), ('Charlie', 10)]
        self.assertEqual(max_aggregate(stdata), ('Alice', 10))

    def test_empty_input(self):
        stdata = []
        with self.assertRaises(TypeError):
            max_aggregate(stdata)

    def test_non_iterable_input(self):
        stdata = 'Invalid input'
        with self.assertRaises(TypeError):
            max_aggregate(stdata)
