import unittest
from mbpp_299_code import max_aggregate

class TestMaxAggregate(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(max_aggregate([]), [])

    def test_single_student(self):
        self.assertEqual(max_aggregate([('Alice', 90)]), [('Alice', 90)])

    def test_multiple_students(self):
        self.assertEqual(max_aggregate([('Alice', 90), ('Bob', 80), ('Charlie', 70)]), [('Alice', 90)])

    def test_students_with_same_marks(self):
        self.assertEqual(max_aggregate([('Alice', 90), ('Bob', 90), ('Charlie', 90)]), [('Alice', 90)])

    def test_students_with_zero_marks(self):
        self.assertEqual(max_aggregate([('Alice', 0), ('Bob', 0), ('Charlie', 0)]), [('Alice', 0)])

    def test_students_with_negative_marks(self):
        self.assertEqual(max_aggregate([('Alice', -10), ('Bob', -20), ('Charlie', -30)]), [('Alice', -10)])

    def test_students_with_max_marks(self):
        self.assertEqual(max_aggregate([('Alice', 100), ('Bob', 100), ('Charlie', 100)]), [('Alice', 100)])

    def test_students_with_min_marks(self):
        self.assertEqual(max_aggregate([('Alice', 0), ('Bob', 0), ('Charlie', 0)]), [('Alice', 0))
