import unittest
from mbpp_722_code import filter_data

class TestFilterData(unittest.TestCase):

    def test_filter_data(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (150, 50)}
        result = filter_data(students, 160, 50)
        expected_result = {'Alice': (160, 55), 'Bob': (170, 60)}
        self.assertEqual(result, expected_result)

    def test_filter_data_empty_students(self):
        students = {}
        result = filter_data(students, 160, 50)
        expected_result = {}
        self.assertEqual(result, expected_result)

    def test_filter_data_no_match(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (150, 50)}
        result = filter_data(students, 180, 65)
        expected_result = {}
        self.assertEqual(result, expected_result)

    def test_filter_data_all_match(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (150, 50)}
        result = filter_data(students, 150, 50)
        expected_result = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (150, 50)}
        self.assertEqual(result, expected_result)
