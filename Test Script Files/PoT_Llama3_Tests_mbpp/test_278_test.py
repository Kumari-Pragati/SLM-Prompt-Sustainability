import unittest
from mbpp_278_code import count_first_elements

class TestCountFirstElements(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_first_elements((1, 2, 3)), 1)

    def test_edge_case_empty_tuple(self):
        self.assertEqual(count_first_elements(()), 0)

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(count_first_elements((1,)), 1)

    def test_edge_case_first_element_tuple(self):
        self.assertEqual(count_first_elements((1, (2, 3))), 1)

    def test_edge_case_last_element_tuple(self):
        self.assertEqual(count_first_elements((1, 2, (3,))), 2)

    def test_edge_case_middle_element_tuple(self):
        self.assertEqual(count_first_elements((1, 2, (3, 4))), 2)

    def test_edge_case_first_element_not_tuple(self):
        self.assertEqual(count_first_elements((1, 2, 3)), 1)

    def test_edge_case_last_element_not_tuple(self):
        self.assertEqual(count_first_elements((1, 2, 3)), 2)

    def test_edge_case_middle_element_not_tuple(self):
        self.assertEqual(count_first_elements((1, 2, 3)), 2)
