import unittest
from mbpp_648_code import exchange_elements

class TestExchangeElements(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5]), [2, 1, 4, 3])
        self.assertEqual(exchange_elements(['a', 'b', 'c', 'd', 'e']), ['b', 'a', 'd', 'c'])

    def test_empty_list(self):
        self.assertEqual(exchange_elements([]), [])

    def test_odd_length(self):
        self.assertEqual(exchange_elements([1]), [])
        self.assertEqual(exchange_elements([1, 2]), [2])
        self.assertEqual(exchange_elements([1, 2, 3]), [2, 1])

    def test_even_length_1(self):
        self.assertEqual(exchange_elements([1, 2]), [2, 1])
        self.assertEqual(exchange_elements([1, 2, 3]), [2, 1, 3])
        self.assertEqual(exchange_elements([1, 2, 3, 4]), [2, 1, 4, 3])

    def test_even_length_2(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5]), [2, 1, 4, 3, 5])
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5, 6]), [2, 1, 4, 3, 6, 5])

    def test_mixed_types(self):
        self.assertEqual(exchange_elements([1, 'a', 2, 'b']), ['a', 1, 'b', 2])

    def test_invalid_input(self):
        self.assertRaises(TypeError, exchange_elements, 123)
