import unittest
from mbpp_648_code import exchange_elements

class TestExchangeElements(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5]), [1, 2, 2, 1, 3, 4, 4, 3, 5, 5])

    def test_edge_case_empty_list(self):
        self.assertEqual(exchange_elements([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(exchange_elements([1]), [1])

    def test_edge_case_even_length_list(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4]), [1, 2, 2, 1, 3, 4])

    def test_edge_case_odd_length_list(self):
        self.assertEqual(exchange_elements([1, 2, 3]), [1, 2, 2, 1, 3])

    def test_edge_case_long_list(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 2, 1, 3, 4, 4, 3, 5, 6, 6, 5, 7, 8, 8, 7, 9, 10, 10, 9])
