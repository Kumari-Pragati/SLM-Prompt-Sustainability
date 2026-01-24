import unittest
from mbpp_119_code import search

class TestSearchFunction(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(search(arr, n), 17)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(search(arr, n), 0)

    def test_single_element_array(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(search(arr, n), 5)

    def test_duplicate_elements(self):
        arr = [1, 2, 3, 2, 1]
        n = len(arr)
        self.assertEqual(search(arr, n), 4)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        self.assertEqual(search(arr, n), -15)

    def test_large_numbers(self):
        arr = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000]
        n = len(arr)
        self.assertEqual(search(arr, n), 16000000000)

    def test_invalid_input_type(self):
        arr = "1, 2, 3, 4, 5"
        n = len(arr)
        with self.assertRaises(TypeError):
            search(arr, n)

    def test_invalid_input_value(self):
        arr = [1, 2, 3, 4, '5']
        n = len(arr)
        with self.assertRaises(TypeError):
            search(arr, n)
