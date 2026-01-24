import unittest
from mbpp_722_code import filter_data

class TestFilterData(unittest.TestCase):

    def test_filter_data(self):
        students = {
            'Alice': [90, 80],
            'Bob': [70, 90],
            'Charlie': [80, 70],
            'David': [100, 90],
            'Eve': [90, 80]
        }
        h = 80
        w = 70
        expected_result = {
            'Alice': [90, 80],
            'David': [100, 90],
            'Eve': [90, 80]
        }
        self.assertEqual(filter_data(students, h, w), expected_result)

    def test_filter_data_empty(self):
        students = {}
        h = 80
        w = 70
        expected_result = {}
        self.assertEqual(filter_data(students, h, w), expected_result)

    def test_filter_data_no_students(self):
        students = {}
        h = 80
        w = 70
        expected_result = {}
        self.assertEqual(filter_data(students, h, w), expected_result)

    def test_filter_data_no_height(self):
        students = {
            'Alice': [90, 80],
            'Bob': [70, 90],
            'Charlie': [80, 70],
            'David': [100, 90],
            'Eve': [90, 80]
        }
        h = None
        w = 70
        expected_result = {
            'Alice': [90, 80],
            'Bob': [70, 90],
            'Charlie': [80, 70],
            'David': [100, 90],
            'Eve': [90, 80]
        }
        self.assertEqual(filter_data(students, h, w), expected_result)

    def test_filter_data_no_width(self):
        students = {
            'Alice': [90, 80],
            'Bob': [70, 90],
            'Charlie': [80, 70],
            'David': [100, 90],
            'Eve': [90, 80]
        }
        h = 80
        w = None
        expected_result = {
            'Alice': [90, 80],
            'Bob': [70, 90],
            'Charlie': [80, 70],
            'David': [100, 90],
            'Eve': [90, 80]
        }
        self.assertEqual(filter_data(students, h, w), expected_result)
