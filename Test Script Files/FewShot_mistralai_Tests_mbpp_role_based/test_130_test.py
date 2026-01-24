import unittest
from mbpp_130_code import defaultdict
from thirteen_0_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(max_occurrences([1]), (1, 1))

    def test_multiple_elements(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3]), (3, 3))

    def test_duplicate_zero(self):
        self.assertEqual(max_occurrences([0, 0, 1]), (0, 2))

    def test_empty_list(self):
        self.assertEqual(max_occurrences([]), (None, None))

    def test_negative_numbers(self):
        self.assertEqual(max_occurrences([-1, -1, 0]), (-1, 2))

    def test_single_negative_number(self):
        self.assertEqual(max_occurrences([-1]), (-1, 1))
