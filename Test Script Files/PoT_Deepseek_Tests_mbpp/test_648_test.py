import unittest
from mbpp_648_code import exchange_elements

class TestExchangeElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5, 6]), [2, 1, 4, 3, 6, 5])

    def test_empty_list(self):
        self.assertEqual(exchange_elements([]), [])

    def test_single_element(self):
        self.assertEqual(exchange_elements([1]), [1])

    def test_even_number_of_elements(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4]), [2, 1, 4, 3])

    def test_odd_number_of_elements(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5]), [2, 1, 4, 3, 5])

    def test_large_number_of_elements(self):
        self.assertEqual(exchange_elements(list(range(1, 101))), list(range(2, 101, 2)) + list(range(1, 100, 2)))
