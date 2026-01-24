import unittest
from mbpp_722_code import filter_data

class TestFilterData(unittest.TestCase):

    def test_normal_case(self):
        students = {
            "Alice": (18, 170),
            "Bob": (20, 180),
            "Charlie": (19, 165),
            "David": (21, 190),
        }
        expected = {
            "Bob": (20, 180),
            "David": (21, 190),
        }
        self.assertDictEqual(filter_data(students, 20, 180), expected)

    def test_edge_case_height(self):
        students = {
            "Alice": (18, 170),
            "Bob": (20, 180),
            "Charlie": (19, 165),
            "David": (21, 190),
        }
        expected = {
            "Alice": (18, 170),
            "Bob": (20, 180),
            "Charlie": (19, 165),
        }
        self.assertDictEqual(filter_data(students, 19, 180), expected)

    def test_edge_case_width(self):
        students = {
            "Alice": (18, 170),
            "Bob": (20, 180),
            "Charlie": (19, 165),
            "David": (21, 190),
        }
        expected = {
            "Bob": (20, 180),
            "David": (21, 190),
        }
        self.assertDictEqual(filter_data(students, 20, 165), expected)

    def test_invalid_input_height(self):
        students = {
            "Alice": (18, 170),
            "Bob": (20, 180),
            "Charlie": (19, 165),
            "David": (21, 190),
        }
        with self.assertRaises(ValueError):
            filter_data(students, -1, 180)

    def test_invalid_input_width(self):
        students = {
            "Alice": (18, 170),
            "Bob": (20, 180),
            "Charlie": (19, 165),
            "David": (21, 190),
        }
        with self.assertRaises(ValueError):
            filter_data(students, 20, -1)
