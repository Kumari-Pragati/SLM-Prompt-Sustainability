import unittest
from mbpp_130_code import defaultdict
from 130_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_occurrences([]), (None, 0))

    def test_single_element(self):
        self.assertEqual(max_occurrences([1]), (1, 1))

    def test_multiple_elements_same_max(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3]), (1, 2))

    def test_multiple_elements_different_max(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 4]), (3, 3))

    def test_negative_numbers(self):
        self.assertEqual(max_occurrences([-1, -1, 0, 1]), (-1, 2))

    def test_floats(self):
        self.assertEqual(max_occurrences([1.1, 1.1, 2.2]), (1.1, 2))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_occurrences(1.3)
