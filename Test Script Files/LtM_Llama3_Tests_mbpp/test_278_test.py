import unittest
from mbpp_278_code import count_first_elements

class TestCountFirstElements(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(count_first_elements(()), 0)

    def test_single_element(self):
        self.assertEqual(count_first_elements((1,)), 1)

    def test_tuple_of_tuples(self):
        self.assertEqual(count_first_elements((1, (2, 3), 4)), 1)

    def test_edge_case_empty_tuple(self):
        self.assertEqual(count_first_elements(()), 0)

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(count_first_elements((1,)), 1)

    def test_edge_case_tuple_of_tuples(self):
        self.assertEqual(count_first_elements((1, (2, 3), 4)), 1)

    def test_edge_case_last_element_tuple(self):
        self.assertEqual(count_first_elements((1, 2, (3, 4))), 2)

    def test_edge_case_first_element_tuple(self):
        self.assertEqual(count_first_elements((1, 2, 3, (4, 5))), 3)

    def test_edge_case_middle_element_tuple(self):
        self.assertEqual(count_first_elements((1, 2, (3, 4), 5)), 2)

    def test_edge_case_last_element_tuple(self):
        self.assertEqual(count_first_elements((1, 2, 3, (4, 5))), 3)

    def test_edge_case_first_element_tuple(self):
        self.assertEqual(count_first_elements((1, 2, 3, (4, 5))), 3)

    def test_edge_case_middle_element_tuple(self):
        self.assertEqual(count_first_elements((1, 2, 3, (4, 5))), 3)

    def test_edge_case_last_element_tuple(self):
        self.assertEqual(count_first_elements((1, 2, 3, (4, 5))), 3)

    def test_edge_case_first_element_tuple(self):
        self.assertEqual(count_first_elements((1, 2, 3, (4, 5))), 3)
