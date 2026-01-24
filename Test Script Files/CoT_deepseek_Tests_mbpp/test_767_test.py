import unittest
from mbpp_767_code import get_Pairs_Count

class TestGetPairsCount(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum = 5
        self.assertEqual(get_Pairs_Count(arr, n, sum), 2)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        sum = 5
        self.assertEqual(get_Pairs_Count(arr, n, sum), 0)

    def test_single_element(self):
        arr = [5]
        n = len(arr)
        sum = 5
        self.assertEqual(get_Pairs_Count(arr, n, sum), 0)

    def test_no_pairs(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum = 10
        self.assertEqual(get_Pairs_Count(arr, n, sum), 0)

    def test_negative_numbers(self):
        arr = [-1, -2, 3, 4, 5]
        n = len(arr)
        sum = 3
        self.assertEqual(get_Pairs_Count(arr, n, sum), 1)

    def test_duplicate_elements(self):
        arr = [1, 2, 2, 3, 4]
        n = len(arr)
        sum = 4
        self.assertEqual(get_Pairs_Count(arr, n, sum), 2)
