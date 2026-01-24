import unittest
from mbpp_722_code import List, Dict
from collections import namedtuple

Student = namedtuple('Student', 'name height weight')

students_data = [
    Student('Alice', 170, 60),
    Student('Bob', 165, 70),
    Student('Charlie', 180, 65),
    Student('David', 175, 55),
    Student('Eve', 160, 75)
]

class TestFilterData(unittest.TestCase):

    def test_filter_data_empty_students(self):
        students = []
        height, width = 180, 65
        result = filter_data(students, height, width)
        self.assertDictEqual(result, {})

    def test_filter_data_no_match(self):
        students = students_data
        height, width = 150, 50
        result = filter_data(students, height, width)
        expected = {Student('David', 175, 55)}
        self.assertDictEqual(result, expected)

    def test_filter_data_single_match(self):
        students = students_data
        height, width = 170, 60
        result = filter_data(students, height, width)
        expected = {Student('Alice', 170, 60)}
        self.assertDictEqual(result, expected)

    def test_filter_data_multiple_matches(self):
        students = students_data
        height, width = 175, 65
        result = filter_data(students, height, width)
        expected = {Student('Alice', 170, 60), Student('Charlie', 180, 65)}
        self.assertDictEqual(result, expected)
