import unittest
from mbpp_722_code import filter_data

class TestFilterData(unittest.TestCase):

    def test_typical_case(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (165, 58)}
        self.assertEqual(filter_data(students, 160, 55), {'Alice': (160, 55), 'Charlie': (165, 58)})

    def test_edge_case(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (165, 58)}
        self.assertEqual(filter_data(students, 160, 55), {'Alice': (160, 55), 'Charlie': (165, 58)})

    def test_boundary_case(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (165, 58)}
        self.assertEqual(filter_data(students, 160, 55), {'Alice': (160, 55), 'Charlie': (165, 58)})

    def test_corner_case(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (165, 58)}
        self.assertEqual(filter_data(students, 160, 55), {'Alice': (160, 55), 'Charlie': (165, 58)})

    def test_invalid_input(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (165, 58)}
        with self.assertRaises(TypeError):
            filter_data(students, 'invalid_height', 55)
