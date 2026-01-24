import unittest
from mbpp_648_code import exchange_elements

class TestExchangeElements(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(exchange_elements([]), [])

    def test_single_element_list(self):
        self.assertEqual(exchange_elements([1]), [1])

    def test_even_length_list(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4]), [1, 2, 2, 1])

    def test_odd_length_list(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5]), [1, 2, 4, 3, 5])

    def test_mixed_length_list(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5, 6, 7, 8]), [1, 2, 4, 3, 6, 5, 8, 7])

    def test_list_with_duplicates(self):
        self.assertEqual(exchange_elements([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), [1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
