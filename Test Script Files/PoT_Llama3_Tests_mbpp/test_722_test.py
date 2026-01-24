import unittest
from mbpp_722_code import filter_data

class TestFilterData(unittest.TestCase):
    def test_typical_case(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [100, 90]}
        h = 80
        w = 70
        expected = {'Alice': [90, 80], 'Charlie': [100, 90]}
        self.assertEqual(filter_data(students, h, w), expected)

    def test_edge_case_h_equal_to_first_student_height(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [100, 90]}
        h = 90
        w = 70
        expected = {'Alice': [90, 80], 'Charlie': [100, 90]}
        self.assertEqual(filter_data(students, h, w), expected)

    def test_edge_case_w_equal_to_first_student_weight(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [100, 90]}
        h = 80
        w = 90
        expected = {'Alice': [90, 80], 'Charlie': [100, 90]}
        self.assertEqual(filter_data(students, h, w), expected)

    def test_edge_case_h_equal_to_second_student_height(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [100, 90]}
        h = 80
        w = 70
        expected = {'Alice': [90, 80], 'Charlie': [100, 90]}
        self.assertEqual(filter_data(students, h, w), expected)

    def test_edge_case_w_equal_to_second_student_weight(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [100, 90]}
        h = 70
        w = 60
        expected = {'Bob': [70, 60]}
        self.assertEqual(filter_data(students, h, w), expected)

    def test_corner_case_h_greater_than_all_student_heights(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [100, 90]}
        h = 110
        w = 70
        expected = {'Charlie': [100, 90]}
        self.assertEqual(filter_data(students, h, w), expected)

    def test_corner_case_w_greater_than_all_student_weights(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [100, 90]}
        h = 80
        w = 110
        expected = {'Alice': [90, 80]}
        self.assertEqual(filter_data(students, h, w), expected)

    def test_invalid_input_type(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [100, 90]}
        h = 'invalid'
        w = 70
        with self.assertRaises(TypeError):
            filter_data(students, h, w)

    def test_invalid_input_value(self):
        students = {'Alice': [90, 80], 'Bob': [70, 60], 'Charlie': [100, 90]}
        h = 100
        w = 'invalid'
        with self.assertRaises(TypeError):
            filter_data(students, h, w)
