import unittest
from mbpp_722_code import filter_data

class TestFilterData(unittest.TestCase):

    def test_typical_case(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (180, 65)}
        self.assertEqual(filter_data(students, 170, 60), {'Bob': (170, 60)})

    def test_edge_case_height(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (180, 65)}
        self.assertEqual(filter_data(students, 150, 50), students)

    def test_edge_case_weight(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (180, 65)}
        self.assertEqual(filter_data(students, 180, 50), students)

    def test_edge_case_both(self):
        students = {'Alice': (160, 55), 'Bob': (170, 60), 'Charlie': (180, 65)}
        self.assertEqual(filter_data(students, 150, 50), {})

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            filter_data("not a dictionary", 170, 60)

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            filter_data({'Alice': (160, 55)}, 170, 60)
