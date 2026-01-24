import unittest
from mbpp_722_code import filter_data

class TestFilterData(unittest.TestCase):
    def test_typical_use_case(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [95, 85]}
        h = 80
        w = 70
        expected_result = {'Alice': [90, 80], 'Charlie': [95, 85]}
        self.assertEqual(filter_data(students, h, w), expected_result)

    def test_edge_case_height_equal_to_first_grade(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [95, 85]}
        h = 90
        w = 70
        expected_result = {'Alice': [90, 80], 'Charlie': [95, 85]}
        self.assertEqual(filter_data(students, h, w), expected_result)

    def test_edge_case_width_equal_to_first_grade(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [95, 85]}
        h = 80
        w = 90
        expected_result = {'Alice': [90, 80], 'Charlie': [95, 85]}
        self.assertEqual(filter_data(students, h, w), expected_result)

    def test_edge_case_height_and_width_equal_to_first_grade(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [95, 85]}
        h = 90
        w = 90
        expected_result = {'Alice': [90, 80], 'Charlie': [95, 85]}
        self.assertEqual(filter_data(students, h, w), expected_result)

    def test_invalid_input_type_height(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [95, 85]}
        h = 'hello'
        w = 70
        with self.assertRaises(TypeError):
            filter_data(students, h, w)

    def test_invalid_input_type_width(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [95, 85]}
        h = 70
        w = 'hello'
        with self.assertRaises(TypeError):
            filter_data(students, h, w)
