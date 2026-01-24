import unittest
from mbpp_722_code import filter_data

class TestFilterData(unittest.TestCase):
    def test_typical_use_case(self):
        students = {
            ("Alice", 18, 175),
            ("Bob", 20, 180),
            ("Charlie", 19, 170),
            ("David", 21, 165),
        }
        expected_result = {
            ("Bob", 20, 180),
            ("Charlie", 19, 170),
            ("David", 21, 165),
        }
        self.assertEqual(filter_data(students, 18, 170), expected_result)

    def test_edge_case_height(self):
        students = {
            ("Alice", 18, 175),
            ("Bob", 20, 180),
            ("Charlie", 19, 170),
            ("David", 21, 165),
        }
        self.assertEqual(filter_data(students, 17, 170), {("Alice", 18, 175)})

    def test_edge_case_width(self):
        students = {
            ("Alice", 18, 175),
            ("Bob", 20, 180),
            ("Charlie", 19, 170),
            ("David", 21, 165),
        }
        self.assertEqual(filter_data(students, 18, 169), {("Alice", 18, 175), ("Bob", 20, 180), ("Charlie", 19, 170)})

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            filter_data(students, -1, 170)

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            filter_data(students, 18, -1)
