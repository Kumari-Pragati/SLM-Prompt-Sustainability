import unittest
from mbpp_25_code import find_Product

class TestFindProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Product([2, 3, 4, 5, 6], 5), 2*3*4*5*6)

    def test_single_element(self):
        self.assertEqual(find_Product([5], 1), 5)

    def test_duplicate_elements(self):
        self.assertEqual(find_Product([2, 2, 3, 4, 4], 5), 2*2*3*4*4)

    def test_negative_elements(self):
        self.assertEqual(find_Product([-2, -3, -4, -5, -6], 5), (-2)*(-3)*(-4)*(-5)*(-6))

    def test_zero_elements(self):
        self.assertEqual(find_Product([0, 1, 2, 3, 4], 5), 0)

    def test_empty_array(self):
        with self.assertRaises(ValueError):
            find_Product([], 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Product("not an array", 0)
