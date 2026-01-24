import unittest
from mbpp_722_code import filter_data

class TestFilterData(unittest.TestCase):
    def test_typical_use_case(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (180, 65)}
        result = filter_data(students, 170, 60)
        self.assertEqual(result, {'Bob': (170, 60), 'Charlie': (180, 65)})

    def test_edge_case_height(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (180, 65)}
        result = filter_data(students, 159, 60)
        self.assertEqual(result, {'Alice': (160, 55), 'Bob': (170, 60)})

    def test_edge_case_weight(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (180, 65)}
        result = filter_data(students, 170, 59)
        self.assertEqual(result, {'Alice': (160, 55), 'Bob': (170, 60)})

    def test_boundary_case_height(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (180, 65)}
        result = filter_data(students, 160, 60)
        self.assertEqual(result, {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (180, 65)})

    def test_boundary_case_weight(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (180, 65)}
        result = filter_data(students, 170, 60)
        self.assertEqual(result, {'Bob': (170, 60), 'Charlie': (180, 65)})

    def test_invalid_input(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (180, 65)}
        with self.assertRaises(TypeError):
            filter_data(students, '170', 60)
