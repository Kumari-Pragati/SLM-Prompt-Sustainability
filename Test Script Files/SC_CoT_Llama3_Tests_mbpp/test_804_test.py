import unittest
from mbpp_804_code import is_Product_Even

class TestIsProductEven(unittest.TestCase):

    def test_typical_input(self):
        self.assertTrue(is_Product_Even([2, 4, 6], 3))

    def test_edge_case(self):
        self.assertFalse(is_Product_Even([1, 3, 5], 3))

    def test_empty_array(self):
        self.assertFalse(is_Product_Even([], 0))

    def test_single_element_array(self):
        self.assertFalse(is_Product_Even([2], 1))

    def test_array_with_single_even_element(self):
        self.assertTrue(is_Product_Even([2, 3, 4], 3))

    def test_array_with_no_even_elements(self):
        self.assertFalse(is_Product_Even([1, 3, 5], 3))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            is_Product_Even("hello", 3)

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            is_Product_Even([1, 2, 3], "hello")

    def test_invalid_input_type3(self):
        with self.assertRaises(TypeError):
            is_Product_Even([1, 2, 3], 3.5)
