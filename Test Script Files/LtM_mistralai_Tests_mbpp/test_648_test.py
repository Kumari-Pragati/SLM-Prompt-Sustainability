import unittest
from mbpp_648_code import exchange_elements

class TestExchangeElements(unittest.TestCase):

    def test_simple_even_length(self):
        self.assertListEqual(exchange_elements([1, 2, 3, 4]), [2, 1, 4, 3])
        self.assertListEqual(exchange_elements([5, 6, 7, 8]), [6, 5, 8, 7])

    def test_simple_odd_length(self):
        self.assertListEqual(exchange_elements([1, 2, 3]), [2, 1, 3])
        self.assertListEqual(exchange_elements([5, 6, 7]), [6, 5, 7])

    def test_edge_cases(self):
        self.assertListEqual(exchange_elements([]), [])
        self.assertListEqual(exchange_elements([1]), [1])
        self.assertListEqual(exchange_elements([1, 2]), [2, 1])
