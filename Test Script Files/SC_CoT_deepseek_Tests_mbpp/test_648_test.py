import unittest
from mbpp_648_code import exchange_elements

class TestExchangeElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5, 6]), [2, 1, 4, 3, 6, 5])

    def test_odd_length_list(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5]), [2, 1, 4, 3, 5])

    def test_empty_list(self):
        self.assertEqual(exchange_elements([]), [])

    def test_single_element_list(self):
        self.assertEqual(exchange_elements([1]), [1])

    def test_two_elements_list(self):
        self.assertEqual(exchange_elements([1, 2]), [2, 1])

    def test_negative_numbers(self):
        self.assertEqual(exchange_elements([-1, -2, -3, -4, -5]), [-2, -1, -4, -3, -5])

    def test_zero(self):
        self.assertEqual(exchange_elements([0, 1, 2, 3]), [1, 0, 2, 3])

    def test_large_numbers(self):
        self.assertEqual(exchange_elements([100, 200, 300, 400]), [200, 100, 400, 300])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            exchange_elements("1, 2, 3, 4")
