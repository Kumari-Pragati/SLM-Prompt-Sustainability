import unittest
from mbpp_648_code import exchange_elements

class TestExchangeElements(unittest.TestCase):

    def test_empty_list(self):
        """Test behavior with an empty list"""
        self.assertEqual(exchange_elements([]), [])

    def test_single_element(self):
        """Test behavior with a single element list"""
        self.assertEqual(exchange_elements([1]), [1])

    def test_even_length_list(self):
        """Test behavior with an even-length list"""
        self.assertEqual(exchange_elements([1, 2, 3, 4]), [2, 1, 4, 3])

    def test_odd_length_list(self):
        """Test behavior with an odd-length list"""
        self.assertEqual(exchange_elements([1, 2, 3]), [2, 1, 3])

    def test_list_with_duplicates(self):
        """Test behavior with a list containing duplicates"""
        self.assertEqual(exchange_elements([1, 2, 2, 3]), [2, 1, 3, 2])

    def test_list_with_non_iterable_element(self):
        """Test behavior with a list containing a non-iterable element"""
        with self.assertRaises(TypeError):
            exchange_elements([1, 2, "non_iterable"])
