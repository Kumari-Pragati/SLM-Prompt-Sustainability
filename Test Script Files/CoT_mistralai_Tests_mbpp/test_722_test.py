import unittest
from mbpp_722_code import filter_data

class TestFilterData(unittest.TestCase):
    def test_empty_list(self):
        self.assertDictEqual(filter_data({}, 1, 1), {})

    def test_single_student(self):
        self.assertDictEqual(filter_data({(1, 1): (1, 1)}, 1, 1), {(1, 1): (1, 1)})

    def test_multiple_students(self):
        students = {(1, 1): (1, 1), (2, 2): (2, 2), (3, 3): (3, 3)}
        self.assertDictEqual(filter_data(students, 2, 2), {(2, 2): (2, 2)})

    def test_students_below_height_and_width(self):
        students = {(1, 1): (1, 1), (2, 2): (2, 2), (3, 3): (3, 3)}
        self.assertDictEqual(filter_data(students, 4, 4), {})

    def test_students_at_height_and_width(self):
        students = {(1, 1): (1, 1), (2, 2): (2, 2), (3, 3): (3, 3)}
        self.assertDictEqual(filter_data(students, 2, 2), {(2, 2): (2, 2)})

    def test_students_above_height_and_width(self):
        students = {(1, 1): (1, 1), (2, 2): (2, 2), (3, 3): (3, 3)}
        self.assertDictEqual(filter_data(students, 4, 4), {})

    def test_students_below_height_and_above_width(self):
        students = {(1, 1): (1, 1), (2, 2): (2, 2), (3, 3): (3, 3)}
        self.assertDictEqual(filter_data(students, 2, 4), {})

    def test_students_above_height_and_below_width(self):
        students = {(1, 1): (1, 1), (2, 2): (2, 2), (3, 3): (3, 3)}
        self.assertDictEqual(filter_data(students, 4, 2), {})

    def test_students_at_height_and_below_width(self):
        students = {(1, 1): (1, 1), (2, 2): (2, 2), (3, 3): (3, 3)}
        self.assertDictEqual(filter_data(students, 2, 1), {})

    def test_students_at_height_and_width_zero(self):
        self.assertDictEqual(filter_data({(1, 1): (1, 1)}, 0, 0), {})

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            filter_data({(1, 1): (1, 1)}, 'h', 1)

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            filter_data({(1, 1): (1, 1)}, 1, 'w')
