import unittest
from mbpp_722_code import filter_data

class TestFilterData(unittest.TestCase):
    def test_simple_input(self):
        students = {'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}
        h = 2
        w = 3
        result = filter_data(students, h, w)
        self.assertEqual(result, {'a': [1, 2], 'c': [5, 6]})

    def test_empty_input(self):
        students = {}
        h = 2
        w = 3
        result = filter_data(students, h, w)
        self.assertEqual(result, {})

    def test_min_values(self):
        students = {'a': [1, 1], 'b': [2, 2], 'c': [3, 3]}
        h = 1
        w = 1
        result = filter_data(students, h, w)
        self.assertEqual(result, {'a': [1, 1]})

    def test_max_values(self):
        students = {'a': [10, 10], 'b': [11, 11], 'c': [12, 12]}
        h = 10
        w = 10
        result = filter_data(students, h, w)
        self.assertEqual(result, {'a': [10, 10], 'b': [11, 11], 'c': [12, 12]})

    def test_invalid_input(self):
        students = {'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}
        h = 'invalid'
        w = 3
        with self.assertRaises(TypeError):
            filter_data(students, h, w)
