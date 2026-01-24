import unittest
from793_code import last

class TestLastFunction(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(last([4, 5, 6, 7, 8], 6, 5), 3)
        self.assertEqual(last([1, 2, 3, 4, 5], 5, 5), 4)
        self.assertEqual(last([10, 20, 30, 40, 50], 30, 5), 2)

    def test_edge_case_empty_list(self):
        self.assertEqual(last([], 10, 0), -1)

    def test_edge_case_single_element(self):
        self.assertEqual(last([10], 10, 1), 0)

    def test_edge_case_first_element(self):
        self.assertEqual(last([10, 20], 10, 2), 0)

    def test_edge_case_last_element(self):
        self.assertEqual(last([10, 20], 20, 2), 1)

    def test_edge_case_element_not_found(self):
        self.assertEqual(last([10, 20], 30, 2), -1)

    def test_edge_case_negative_number(self):
        self.assertEqual(last([-10, -20], -30, 2), -1)

    def test_edge_case_out_of_bounds_index(self):
        self.assertEqual(last([10, 20], 30, 6), -1)
