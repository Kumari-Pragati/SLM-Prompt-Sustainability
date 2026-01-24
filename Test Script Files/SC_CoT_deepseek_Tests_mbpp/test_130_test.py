import unittest
from mbpp_130_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), (3, 3))

    def test_single_element(self):
        self.assertEqual(max_occurrences([1]), (1, 1))

    def test_empty_list(self):
        self.assertEqual(max_occurrences([]), None)

    def test_negative_numbers(self):
        self.assertEqual(max_occurrences([-1, -2, -2, -3, -3]), (-1, 1))

    def test_duplicates(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3, 3]), (3, 4))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_occurrences('123')
