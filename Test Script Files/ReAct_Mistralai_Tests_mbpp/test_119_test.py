import unittest
from mbpp_119_code import search

class TestSearchFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(search([]))

    def test_single_element_list(self):
        for num in range(10):
            self.assertEqual(search([num]), num)

    def test_multiple_elements_list(self):
        arr = [1, 2, 3, 4, 5]
        expected_xor = 1 ^ 2 ^ 3 ^ 4 ^ 5
        self.assertEqual(search(arr), expected_xor)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, 4, 5]
        expected_xor = -1 ^ -2 ^ -3 ^ 4 ^ 5
        self.assertEqual(search(arr), expected_xor)

    def test_zero_in_list(self):
        arr = [0, 1, 2, 3, 4]
        expected_xor = 1 ^ 2 ^ 3 ^ 4
        self.assertEqual(search(arr), expected_xor)

    def test_duplicate_numbers(self):
        arr = [1, 1, 2, 3, 4]
        expected_xor = 1 ^ 2 ^ 3 ^ 4
        self.assertEqual(search(arr), expected_xor)

    def test_large_input(self):
        arr = [i for i in range(100)]
        expected_xor = functools.reduce(operator.xor, arr)
        self.assertEqual(search(arr), expected_xor)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            search([-1, -2, -3], 0)

    def test_empty_input_length(self):
        with self.assertRaises(ValueError):
            search([], 1)
