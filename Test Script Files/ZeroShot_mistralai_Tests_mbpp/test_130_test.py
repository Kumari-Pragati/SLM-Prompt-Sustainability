import unittest
from mbpp_130_code import defaultdict

def max_occurrences(nums):
    dict = defaultdict(int)
    for i in nums:
        dict[i] += 1
    result = max(dict.items(), key=lambda x: x[1])
    return result

class TestMaxOccurrences(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_occurrences([]))

    def test_single_element(self):
        self.assertEqual(max_occurrences([1]), (1, 1))

    def test_multiple_elements(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3, 3]), (3, 3))

    def test_duplicate_elements(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 2, 3, 3, 3, 3, 3]), (3, 5))

    def test_negative_numbers(self):
        self.assertEqual(max_occurrences([-1, -1, -2, -2, 1]), (-1, 2))
