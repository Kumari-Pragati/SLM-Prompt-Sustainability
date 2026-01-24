import unittest
from mbpp_722_code import filter_data

class TestFilterData(unittest.TestCase):

    def test_typical_case(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (165, 58)}
        result = filter_data(students, 160, 55)
        self.assertEqual(result, {'Alice': (160, 55), 'Charlie': (165, 58)})

    def test_edge_case_height(self):
        students = {'Alice': (150, 55), 'Bob': (160, 60), 'Charlie': (170, 58)}
        result = filter_data(students, 160, 55)
        self.assertEqual(result, {'Bob': (160, 60)})

    def test_edge_case_weight(self):
        students = {'Alice': (160, 50), 'Bob': (170, 60), 'Charlie': (165, 65)}
        result = filter_data(students, 160, 55)
        self.assertEqual(result, {'Bob': (170, 60), 'Charlie': (165, 65)})

    def test_boundary_case(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (165, 58)}
        result = filter_data(students, 160, 55)
        self.assertEqual(result, {'Alice': (160, 55), 'Charlie': (165, 58)})

    def test_invalid_input(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (165, 58)}
        with self.assertRaises(TypeError):
            filter_data(students, '160', 55)
