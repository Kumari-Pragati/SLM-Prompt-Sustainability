import unittest
from mbpp_856_code import find_Min_Swaps

class TestFindMinSwaps(unittest.TestCase):

    def test_typical_case(self):
        arr = [0, 1, 0, 1, 1, 0]
        n = len(arr)
        self.assertEqual(find_Min_Swaps(arr, n), 1)

    def test_all_zeros(self):
        arr = [0, 0, 0, 0]
        n = len(arr)
        self.assertEqual(find_Min_Swaps(arr, n), 0)

    def test_all_ones(self):
        arr = [1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(find_Min_Swaps(arr, n), 0)

    def test_mixed_zeros_and_ones(self):
        arr = [0, 1, 0, 1, 1, 0, 1]
        n = len(arr)
        self.assertEqual(find_Min_Swaps(arr, n), 2)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(find_Min_Swaps(arr, n), 0)

    def test_single_element(self):
        arr = [0]
        n = len(arr)
        self.assertEqual(find_Min_Swaps(arr, n), 0)

    def test_two_elements_same(self):
        arr = [0, 0]
        n = len(arr)
        self.assertEqual(find_Min_Swaps(arr, n), 0)

    def test_two_elements_diff(self):
        arr = [0, 1]
        n = len(arr)
        self.assertEqual(find_Min_Swaps(arr, n), 1)
