import unittest
from mbpp_658_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), 3)

    def test_edge_condition_empty_list(self):
        self.assertIsNone(max_occurrences([]))

    def test_boundary_condition_single_element(self):
        self.assertEqual(max_occurrences([1]), 1)

    def test_complex_input(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), 4)

    def test_same_occurrences(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 4]), 2)
