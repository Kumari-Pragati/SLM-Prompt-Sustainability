import unittest
from mbpp_278_code import count_first_elements

class TestCountFirstElements(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4, 5)), 5)

    def test_edge_case_empty_tuple(self):
        self.assertEqual(count_first_elements(()), 0)

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(count_first_elements((1,)), 1)

    def test_edge_case_tuple_in_middle(self):
        self.assertEqual(count_first_elements((1, 2, (3, 4), 5)), 3)

    def test_edge_case_tuple_at_end(self):
        self.assertEqual(count_first_elements((1, 2, 3, (4, 5))), 4)

    def test_edge_case_tuple_as_first_element(self):
        self.assertEqual(count_first_elements(((1, 2), 3, 4, 5)), 1)

    def test_edge_case_tuple_as_last_element(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4, (5, 6))), 5)

    def test_edge_case_tuple_as_second_element(self):
        self.assertEqual(count_first_elements((1, (2, 3), 4, 5)), 2)

    def test_edge_case_tuple_as_third_element(self):
        self.assertEqual(count_first_elements((1, 2, (3, 4), 5)), 3)

    def test_invalid_input_non_iterable(self):
        with self.assertRaises(TypeError):
            count_first_elements("hello")

    def test_invalid_input_non_iterable_non_string(self):
        with self.assertRaises(TypeError):
            count_first_elements(123)
