import unittest
from mbpp_468_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(max_product(arr, n), 60)

    def test_single_element(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(max_product(arr, n), 5)

    def test_negative_elements(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        self.assertEqual(max_product(arr, n), -1)

    def test_mixed_elements(self):
        arr = [-1, -2, 3, 4, -5]
        n = len(arr)
        self.assertEqual(max_product(arr, n), 40)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(max_product(arr, n), 0)

    def test_large_numbers(self):
        arr = [100, 200, 300, 400, 500]
        n = len(arr)
        self.assertEqual(max_product(arr, n), 12000000000000)

    def test_duplicate_elements(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(max_product(arr, n), 1)
