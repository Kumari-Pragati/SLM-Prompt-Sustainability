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

    def test_long_list(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 4, 3, 6, 5, 8, 7, 10, 9])

    def test_list_with_duplicates(self):
        self.assertEqual(exchange_elements([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), [1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

    def test_list_with_negative_numbers(self):
        self.assertEqual(exchange_elements([-1, -2, -3, -4]), [-1, -2, -4, -3])

    def test_list_with_mixed_types(self):
        self.assertEqual(exchange_elements([1, 'a', 2, 'b', 3, 'c']), [1, 'a', 2, 'c', 'b', 3])
