import unittest
from mbpp_722_code import filter_data

class TestFilterData(unittest.TestCase):
    def test_typical_input(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [95, 85]}
        h = 80
        w = 70
        result = filter_data(students, h, w)
        self.assertEqual(result, {'Alice': [90, 80], 'Charlie': [95, 85]})

    def test_edge_case_height(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [95, 85]}
        h = 90
        w = 70
        result = filter_data(students, h, w)
        self.assertEqual(result, {'Alice': [90, 80], 'Charlie': [95, 85]})

    def test_edge_case_width(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [95, 85]}
        h = 80
        w = 90
        result = filter_data(students, h, w)
        self.assertEqual(result, {'Alice': [90, 80], 'Charlie': [95, 85]})

    def test_edge_case_height_and_width(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [95, 85]}
        h = 90
        w = 90
        result = filter_data(students, h, w)
        self.assertEqual(result, {'Alice': [90, 80], 'Charlie': [95, 85]})

    def test_empty_input(self):
        students = {}
        h = 80
        w = 70
        result = filter_data(students, h, w)
        self.assertEqual(result, {})

    def test_invalid_input_type(self):
        students = {'Alice': [90, 80]}
        h = '80'
        w = 70
        with self.assertRaises(TypeError):
            filter_data(students, h, w)

    def test_invalid_input_value(self):
        students = {'Alice': [90, 80]}
        h = 120
        w = 70
        with self.assertRaises(ValueError):
            filter_data(students, h, w)
