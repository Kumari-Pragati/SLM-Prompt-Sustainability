import unittest
from mbpp_722_code import filter_data

class TestFilterData(unittest.TestCase):

    def test_simple_input(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60)}
        result = filter_data(students, 160, 55)
        self.assertEqual(result, {'Alice': (160, 55)})

    def test_edge_conditions(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60)}
        result = filter_data(students, 0, 0)
        self.assertEqual(result, students)

        result = filter_data(students, 180, 70)
        self.assertEqual(result, {})

    def test_complex_cases(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (180, 70)}
        result = filter_data(students, 170, 60)
        self.assertEqual(result, {'Bob': (170, 60), 'Charlie': (180, 70)})

        result = filter_data(students, 180, 70)
        self.assertEqual(result, {'Charlie': (180, 70)})
