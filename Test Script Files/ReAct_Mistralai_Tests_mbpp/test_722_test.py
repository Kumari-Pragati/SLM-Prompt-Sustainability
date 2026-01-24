import unittest
from mbpp_722_code import filter_data

class TestFilterData(unittest.TestCase):

    def test_filter_data_positive(self):
        students = {
            ("Alice", 18, 175),
            ("Bob", 20, 180),
            ("Charlie", 19, 170),
            ("David", 21, 165),
            ("Eve", 17, 160)
        }
        expected_result = {
            ("Bob", 20, 180),
            ("Charlie", 19, 170),
            ("David", 21, 165)
        }
        self.assertDictEqual(filter_data(students, 18, 170), expected_result)

    def test_filter_data_empty(self):
        students = {}
        self.assertDictEqual(filter_data(students, 18, 170), {})

    def test_filter_data_min_height(self):
        students = {
            ("Alice", 18, 175),
            ("Bob", 20, 180),
            ("Charlie", 19, 170),
            ("David", 21, 165),
            ("Eve", 17, 160)
        }
        self.assertDictEqual(filter_data(students, 22, 170), {})

    def test_filter_data_min_width(self):
        students = {
            ("Alice", 18, 175),
            ("Bob", 20, 180),
            ("Charlie", 19, 170),
            ("David", 21, 165),
            ("Eve", 17, 160)
        }
        self.assertDictEqual(filter_data(students, 18, 160), {("Alice", 18, 175)})

    def test_filter_data_edge_cases(self):
        students = {
            ("Alice", 18, 175),
            ("Bob", 20, 180),
            ("Charlie", 19, 170),
            ("David", 21, 165),
            ("Eve", 17, 160)
        }
        self.assertDictEqual(filter_data(students, 18, 170), {
            ("Bob", 20, 180),
            ("Charlie", 19, 170),
            ("David", 21, 165)
        })
        self.assertDictEqual(filter_data(students, 17, 170), {("Alice", 18, 175)})
        self.assertDictEqual(filter_data(students, 20, 170), {("Bob", 20, 180)})
        self.assertDictEqual(filter_data(students, 18, 169), {("Bob", 20, 180), ("Charlie", 19, 170), ("David", 21, 165)})
        self.assertDictEqual(filter_data(students, 18, 171), {("Bob", 20, 180), ("Charlie", 19, 170)})
