import unittest
from mbpp_278_code import count_first_elements

class TestCountFirstElements(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4)), 3)

    def test_edge_case_empty_tuple(self):
        self.assertEqual(count_first_elements(()), 0)

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(count_first_elements((1,)), 1)

    def test_edge_case_single_element_non_tuple(self):
        self.assertEqual(count_first_elements((1, 2, 3)), 3)

    def test_edge_case_multiple_non_tuple_elements(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4, 5)), 5)

    def test_edge_case_multiple_tuple_elements(self):
        self.assertEqual(count_first_elements((1, (2, 3), 4, 5)), 2)

    def test_edge_case_multiple_nested_tuple_elements(self):
        self.assertEqual(count_first_elements((1, (2, 3), 4, (5, 6))), 3)

    def test_invalid_input_non_iterable(self):
        with self.assertRaises(TypeError):
            count_first_elements("Invalid input")

    def test_invalid_input_non_iterable_with_non_iterable(self):
        with self.assertRaises(TypeError):
            count_first_elements([1, 2, 3, "Invalid input"])
