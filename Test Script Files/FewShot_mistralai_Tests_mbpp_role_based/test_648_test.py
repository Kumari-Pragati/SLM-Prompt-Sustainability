import unittest
from mbpp_648_code import exchange_elements

class TestExchangeElements(unittest.TestCase):
    def test_even_length_list(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4]), [2, 1, 4, 3])

    def test_odd_length_list(self):
        self.assertEqual(exchange_elements([1, 2, 3]), [2, 1, None])

    def test_empty_list(self):
        self.assertEqual(exchange_elements([]), [])

    def test_single_element_list(self):
        self.assertEqual(exchange_elements([1]), [None])
