import unittest
from mbpp_867_code import min_Num

class TestMinNum(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 2)

    def test_odd_count(self):
        arr = [1, 3, 5]
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 1)

    def test_even_count(self):
        arr = [2, 4, 6]
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 2)

    def test_mixed_case(self):
        arr = [1, 2, 3, 4, 5, 6]
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 2)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 2)

    def test_single_element(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 2)

    def test_negative_numbers(self):
        arr = [-1, -3, -5]
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 2)

    def test_zero(self):
        arr = [0, 2, 4]
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 2)
