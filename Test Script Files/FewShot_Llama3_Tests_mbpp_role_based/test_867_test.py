import unittest
from mbpp_867_code import min_Num

class TestMin_Num(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 2)

    def test_odd_number_of_odd_numbers(self):
        arr = [1, 3, 5, 7, 9]
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 1)

    def test_even_number_of_odd_numbers(self):
        arr = [1, 3, 5, 7]
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 2)

    def test_all_even_numbers(self):
        arr = [2, 4, 6, 8]
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 2)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 2)

    def test_array_with_one_element(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 2)
