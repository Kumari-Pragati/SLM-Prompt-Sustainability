import unittest
from mbpp_722_code import filter_data

class TestFilterData(unittest.TestCase):
    def test_typical_case(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [100, 90]}
        h = 80
        w = 70
        expected_result = {'Alice': [90, 80], 'Charlie': [100, 90]}
        self.assertEqual(filter_data(students, h, w), expected_result)

    def test_edge_case_height(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [100, 90]}
        h = 100
        w = 70
        expected_result = {'Charlie': [100, 90]}
        self.assertEqual(filter_data(students, h, w), expected_result)

    def test_edge_case_weight(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [100, 90]}
        h = 80
        w = 100
        expected_result = {'Alice': [90, 80]}
        self.assertEqual(filter_data(students, h, w), expected_result)

    def test_edge_case_height_and_weight(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [100, 90]}
        h = 100
        w = 100
        expected_result = {'Charlie': [100, 90]}
        self.assertEqual(filter_data(students, h, w), expected_result)

    def test_empty_students(self):
        students = {}
        h = 80
        w = 70
        expected_result = {}
        self.assertEqual(filter_data(students, h, w), expected_result)

    def test_empty_height_and_weight(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [100, 90]}
        h = None
        w = None
        expected_result = students
        self.assertEqual(filter_data(students, h, w), expected_result)
