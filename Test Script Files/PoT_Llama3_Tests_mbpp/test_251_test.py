import unittest
from mbpp_251_code import insert_element

class TestInsertElement(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(insert_element([1, 2, 3], 4), [1, 2, 3, 4])

    def test_edge_case_empty_list(self):
        self.assertEqual(insert_element([], 4), [4])

    def test_edge_case_single_element_list(self):
        self.assertEqual(insert_element([1], 2), [1, 2])

    def test_edge_case_element_at_end(self):
        self.assertEqual(insert_element([1, 2, 3], 3), [1, 2, 3, 3])

    def test_edge_case_element_at_start(self):
        self.assertEqual(insert_element([1, 2, 3], 1), [1, 1, 2, 3])

    def test_edge_case_element_in_middle(self):
        self.assertEqual(insert_element([1, 2, 3], 2), [1, 2, 2, 3])

    def test_edge_case_element_at_start_and_end(self):
        self.assertEqual(insert_element([1, 2, 3], 1), [1, 1, 2, 3, 1])

    def test_edge_case_element_at_start_and_middle(self):
        self.assertEqual(insert_element([1, 2, 3], 2), [1, 2, 2, 3, 2])

    def test_edge_case_element_at_start_and_end_and_middle(self):
        self.assertEqual(insert_element([1, 2, 3], 2), [1, 2, 2, 3, 2])

    def test_edge_case_element_at_start_and_end_and_middle_and_start(self):
        self.assertEqual(insert_element([1, 2, 3], 1), [1, 1, 2, 3, 1, 1])

    def test_edge_case_element_at_start_and_end_and_middle_and_start_and_end(self):
        self.assertEqual(insert_element([1, 2, 3], 1), [1, 1, 2, 3, 1, 1, 1])
