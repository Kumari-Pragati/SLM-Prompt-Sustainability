import unittest
from mbpp_648_code import exchange_elements

class TestExchangeElements(unittest.TestCase):
    def test_typical_use_case(self):
        lst = [1, 2, 3, 4, 5, 6]
        expected_result = [1, 2, 4, 3, 5, 6]
        self.assertEqual(exchange_elements(lst), expected_result)

    def test_edge_case_empty_list(self):
        lst = []
        expected_result = []
        self.assertEqual(exchange_elements(lst), expected_result)

    def test_edge_case_single_element_list(self):
        lst = [1]
        expected_result = [1]
        self.assertEqual(exchange_elements(lst), expected_result)

    def test_edge_case_even_length_list(self):
        lst = [1, 2, 3, 4]
        expected_result = [1, 2, 4, 3]
        self.assertEqual(exchange_elements(lst), expected_result)

    def test_edge_case_odd_length_list(self):
        lst = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 4, 3, 5]
        self.assertEqual(exchange_elements(lst), expected_result)
