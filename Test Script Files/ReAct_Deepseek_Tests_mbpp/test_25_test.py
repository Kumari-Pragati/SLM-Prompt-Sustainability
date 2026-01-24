import unittest
from mbpp_25_code import find_Product

class TestFindProduct(unittest.TestCase):

    def test_typical_case(self):
        arr = [2, 3, 4, 5, 6]
        n = len(arr)
        self.assertEqual(find_Product(arr, n), 720)

    def test_single_element(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(find_Product(arr, n), 5)

    def test_duplicate_elements(self):
        arr = [2, 2, 3, 3, 4, 4]
        n = len(arr)
        self.assertEqual(find_Product(arr, n), 24)

    def test_negative_elements(self):
        arr = [-2, -3, -4, -5]
        n = len(arr)
        self.assertEqual(find_Product(arr, n), -120)

    def test_mixed_elements(self):
        arr = [-2, 3, -4, 5]
        n = len(arr)
        self.assertEqual(find_Product(arr, n), -120)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(find_Product(arr, n), 1)

    def test_large_numbers(self):
        arr = [10**6, 10**7, 10**8]
        n = len(arr)
        self.assertEqual(find_Product(arr, n), 10**21)

    def test_large_negative_numbers(self):
        arr = [-10**6, -10**7, -10**8]
        n = len(arr)
        self.assertEqual(find_Product(arr, n), -10**21)

    def test_large_mixed_numbers(self):
        arr = [-10**6, 10**7, -10**8]
        n = len(arr)
        self.assertEqual(find_Product(arr, n), -10**21)
