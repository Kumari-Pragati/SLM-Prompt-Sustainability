import unittest
from mbpp_299_code import max_aggregate

class TestMaxAggregate(unittest.TestCase):

    def test_single_student(self):
        stdata = [('Alice', 90)]
        self.assertEqual(max_aggregate(stdata)[0][1], 90)

    def test_multiple_students(self):
        stdata = [('Alice', 90), ('Bob', 80), ('Charlie', 70)]
        self.assertEqual(max_aggregate(stdata)[0][1], 90)

    def test_tied_max(self):
        stdata = [('Alice', 90), ('Bob', 90), ('Charlie', 80)]
        self.assertEqual(max_aggregate(stdata)[0][1], 90)

    def test_empty_input(self):
        stdata = []
        with self.assertRaises(TypeError):
            max_aggregate(stdata)

    def test_non_iterable_input(self):
        stdata = "Invalid input"
        with self.assertRaises(TypeError):
            max_aggregate(stdata)
