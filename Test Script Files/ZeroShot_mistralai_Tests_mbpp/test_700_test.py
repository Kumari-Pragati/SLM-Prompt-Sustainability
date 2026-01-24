import unittest
from mbpp_700_code import List, Tuple

def count_range_in_list(li: List[int], min: int, max: int) -> int:
    ctr = 0
    for x in li:
        if min <= x <= max:
            ctr += 1
    return ctr

class TestCountRangeInList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_range_in_list([], 1, 2), 0)

    def test_single_element_outside_range(self):
        self.assertEqual(count_range_in_list([3], 1, 2), 0)

    def test_single_element_inside_range(self):
        self.assertEqual(count_range_in_list([5], 1, 5), 1)

    def test_single_element_equal_to_min(self):
        self.assertEqual(count_range_in_list([1], 1, 1), 1)

    def test_single_element_equal_to_max(self):
        self.assertEqual(count_range_in_list([10], 9, 10), 1)

    def test_multiple_elements_in_range(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 1, 5), 4)

    def test_multiple_elements_outside_range(self):
        self.assertEqual(count_range_in_list([-1, 0, 11, 12], 1, 5), 0)

    def test_multiple_elements_below_min(self):
        self.assertEqual(count_range_in_list([-1, -2, -3], 1, 5), 0)

    def test_multiple_elements_above_max(self):
        self.assertEqual(count_range_in_list([16, 17, 18], 1, 5), 0)
