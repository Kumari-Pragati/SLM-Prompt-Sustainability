import unittest
from mbpp_722_code import filter_data

class TestFilterData(unittest.TestCase):

    def test_typical_case(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (180, 65)}
        result = filter_data(students, 170, 60)
        self.assertEqual(result, {'Bob': (170, 60), 'Charlie': (180, 65)})

    def test_edge_case_same_height(self):
        students = {'Alice': (160, 55), 'Bob': (160, 60), 'Charlie': (180, 65)}
        result = filter_data(students, 160, 60)
        self.assertEqual(result, {'Alice': (160, 55), 'Bob': (160, 60)})

    def test_edge_case_same_weight(self):
        students = {'Alice': (160, 55), 'Bob': (170, 55), 'Charlie': (180, 55)}
        result = filter_data(students, 170, 55)
        self.assertEqual(result, {'Alice': (160, 55), 'Bob': (170, 55), 'Charlie': (180, 55)})

    def test_edge_case_same_height_and_weight(self):
        students = {'Alice': (160, 55), 'Bob': (160, 55), 'Charlie': (160, 55)}
        result = filter_data(students, 160, 55)
        self.assertEqual(result, {'Alice': (160, 55), 'Bob': (160, 55), 'Charlie': (160, 55)})

    def test_empty_students(self):
        students = {}
        result = filter_data(students, 170, 60)
        self.assertEqual(result, {})

    def test_error_case_negative_height(self):
        students = {'Alice': (-160, 55), 'Bob': (170, 60), 'Charlie': (180, 65)}
        with self.assertRaises(ValueError):
            filter_data(students, -170, 60)

    def test_error_case_negative_weight(self):
        students = {'Alice': (160, -55), 'Bob': (170, 60), 'Charlie': (180, 65)}
        with self.assertRaises(ValueError):
            filter_data(students, 170, -60)
