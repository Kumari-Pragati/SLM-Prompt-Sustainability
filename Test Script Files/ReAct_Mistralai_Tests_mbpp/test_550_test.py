import unittest
from mbpp_550_code import find_Max

class TestFindMax(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_Max([], 0, 0), None)

    def test_single_element_list(self):
        for element in range(100):
            self.assertEqual(find_Max([element], 0, 0), element)

    def test_multiple_elements_ascending(self):
        for arr in [(list(range(10)), 0, 9), (list(range(-10, 0)), 9, 0), (list(range(100)), 0, 99)]:
            self.assertEqual(find_Max(arr[0], arr[1], arr[2]), arr[0][arr[1]])

    def test_multiple_elements_descending(self):
        for arr in [(list(range(10, 0, -1)), 0, 9), (list(range(100, 0, -1)), 0, 99)]:
            self.assertEqual(find_Max(arr[0], arr[1], arr[2]), arr[0][arr[1]])

    def test_multiple_elements_mixed(self):
        for arr in [(list(range(10, 20)), 0, 9), (list(range(100, 80, -1)), 0, 89)]:
            self.assertEqual(find_Max(arr[0], arr[1], arr[2]), max(arr[0]))

    def test_duplicate_max_element(self):
        for arr in [(list(range(10)), 5, 5), (list(range(100)), 50, 50)]:
            self.assertEqual(find_Max(arr[0], arr[1], arr[2]), max(arr[0]))

    def test_negative_indices(self):
        for arr in [(-10, -1, -1), (-10, 0, -10), (-10, -2, -10), (-10, -10, -10)]:
            self.assertEqual(find_Max(list(range(-10, 0)), *arr), 0)

    def test_out_of_range_indices(self):
        arr = list(range(100))
        self.assertEqual(find_Max(arr, 101, 101), None)
        self.assertEqual(find_Max(arr, -1, -1), None)
