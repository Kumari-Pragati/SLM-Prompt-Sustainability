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

    def test_mixed_numbers(self):
        arr = [1, 2, 3, 4, 6]
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 1)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 2)

    def test_single_odd_number(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 1)

    def test_single_even_number(self):
        arr = [2]
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 2)
