import unittest
from mbpp_648_code import exchange_elements

class TestExchangeElements(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5]), [2, 1, 4, 3, 5])

    def test_empty_input(self):
        self.assertEqual(exchange_elements([]), [])

    def test_single_element_input(self):
        self.assertEqual(exchange_elements([1]), [1])

    def test_even_length_input(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4]), [2, 1, 4, 3])

    def test_odd_length_input(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5]), [2, 1, 4, 3, 5])

    def test_large_input(self):
        self.assertEqual(exchange_elements(list(range(1, 101))), list(range(2, 101, 2)) + list(range(1, 100, 2)))
