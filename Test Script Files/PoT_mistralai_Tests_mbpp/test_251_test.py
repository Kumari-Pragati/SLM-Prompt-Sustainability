import unittest
from mbpp_251_code import insert_element

class TestInsertElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(insert_element([1, 2, 3], 4), [1, 2, 4, 3])
        self.assertEqual(insert_element([], 1), [1])
        self.assertEqual(insert_element([1], 2), [1, 2])

    def test_edge_case_single_element(self):
        self.assertEqual(insert_element([1], 1), [1, 1])

    def test_edge_case_empty_list(self):
        self.assertEqual(insert_element([], 1), [1])

    def test_edge_case_single_element_list(self):
        self.assertEqual(insert_element([1], 2), [1, 2])

    def test_edge_case_duplicate_element(self):
        self.assertEqual(insert_element([1, 1], 2), [1, 1, 2, 1])

    def test_corner_case_negative_number(self):
        self.assertEqual(insert_element([1, 2, 3], -1), [1, 2, -1, 3])
