import unittest
from mbpp_648_code import exchange_elements

class TestExchangeElements(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5]), [1, 2, 4, 3, 5])

    def test_edge_case_empty_list(self):
        self.assertEqual(exchange_elements([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(exchange_elements([1]), [1])

    def test_edge_case_two_element_list(self):
        self.assertEqual(exchange_elements([1, 2]), [1, 2])

    def test_edge_case_odd_length_list(self):
        self.assertEqual(exchange_elements([1, 3, 5, 7, 9]), [1, 1, 3, 5, 7, 9])

    def test_edge_case_even_length_list(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4]), [1, 2, 4, 3])

    def test_edge_case_negative_numbers(self):
        self.assertEqual(exchange_elements([-1, -2, -3, -4]), [-1, -2, -4, -3])

    def test_edge_case_mixed_positive_and_negative_numbers(self):
        self.assertEqual(exchange_elements([-1, 2, -3, 4]), [-1, 2, 4, -3])

    def test_edge_case_mixed_positive_and_negative_numbers_with_zero(self):
        self.assertEqual(exchange_elements([-1, 2, 0, -3, 4]), [-1, 2, 0, 4, -3])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            exchange_elements("hello")
