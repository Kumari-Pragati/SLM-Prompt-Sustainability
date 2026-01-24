import unittest
from mbpp_722_code import filter_data

class TestFilterData(unittest.TestCase):
    def test_typical_case(self):
        students = {
            "Alice": (18, 170),
            "Bob": (20, 180),
            "Charlie": (19, 165),
            "David": (22, 190),
        }
        expected = {
            "Alice": (18, 170),
            "Bob": (20, 180),
            "Charlie": (19, 165),
        }
        self.assertDictEqual(filter_data(students, 18, 165), expected)

    def test_edge_case_height(self):
        students = {
            "Eve": (18, 170),
            "Frank": (17, 180),
            "Grace": (19, 165),
            "Harry": (18, 164),
        }
        expected = {
            "Eve": (18, 170),
            "Frank": (17, 180),
            "Grace": (19, 165),
        }
        self.assertDictEqual(filter_data(students, 18, 165), expected)

    def test_edge_case_width(self):
        students = {
            "Ivy": (18, 170),
            "Jack": (20, 169),
            "Lily": (19, 165),
            "Oliver": (18, 164),
        }
        expected = {
            "Ivy": (18, 170),
            "Jack": (20, 169),
            "Lily": (19, 165),
        }
        self.assertDictEqual(filter_data(students, 18, 165), expected)

    def test_corner_case_both(self):
        students = {
            "Peter": (17, 169),
            "Quincy": (18, 168),
            "Rachel": (19, 165),
            "Sam": (18, 164),
        }
        expected = {
            "Peter": (17, 169),
            "Quincy": (18, 168),
            "Rachel": (19, 165),
        }
        self.assertDictEqual(filter_data(students, 18, 165), expected)
