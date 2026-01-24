import unittest
from mbpp_722_code import filter_data

class TestFilterData(unittest.TestCase):

    def test_typical_input(self):
        students = {'A': [10, 20], 'B': [15, 30], 'C': [5, 10]}
        h = 10
        w = 20
        result = filter_data(students, h, w)
        self.assertEqual(result, {'A': [10, 20], 'B': [15, 30]})

    def test_edge_case_height(self):
        students = {'A': [10, 20], 'B': [15, 30], 'C': [5, 10]}
        h = 5
        w = 20
        result = filter_data(students, h, w)
        self.assertEqual(result, {'A': [10, 20], 'B': [15, 30]})

    def test_edge_case_width(self):
        students = {'A': [10, 20], 'B': [15, 30], 'C': [5, 10]}
        h = 10
        w = 5
        result = filter_data(students, h, w)
        self.assertEqual(result, {'A': [10, 20], 'B': [15, 30]})

    def test_edge_case_height_and_width(self):
        students = {'A': [10, 20], 'B': [15, 30], 'C': [5, 10]}
        h = 5
        w = 5
        result = filter_data(students, h, w)
        self.assertEqual(result, {'A': [10, 20], 'B': [15, 30]})

    def test_invalid_input_type(self):
        students = {'A': [10, 20], 'B': [15, 30], 'C': [5, 10]}
        h = 'ten'
        w = 20
        with self.assertRaises(TypeError):
            filter_data(students, h, w)

    def test_invalid_input_value(self):
        students = {'A': [10, 20], 'B': [15, 30], 'C': [5, 10]}
        h = 100
        w = 100
        result = filter_data(students, h, w)
        self.assertEqual(result, {})
