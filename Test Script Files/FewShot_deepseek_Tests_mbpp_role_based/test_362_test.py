import unittest
from mbpp_362_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), 3)

    def test_edge_case_single_element(self):
        self.assertEqual(max_occurrences([1]), 1)

    def test_boundary_case_empty_list(self):
        self.assertIsNone(max_occurrences([]))

    def test_boundary_case_large_list(self):
        large_list = [i%10 for i in range(10000)]
        self.assertEqual(max_occurrences(large_list), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_occurrences('not a list')
