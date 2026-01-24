import unittest
from mbpp_730_code import consecutive_duplicates

class TestConsecutiveDuplicates(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(consecutive_duplicates([1, 1, 2, 2, 3, 3]), [1, 2, 3])

    def test_edge_condition(self):
        self.assertEqual(consecutive_duplicates([]), [])

    def test_boundary_condition(self):
        self.assertEqual(consecutive_duplicates([1]), [1])
        self.assertEqual(consecutive_duplicates([1, 1]), [1])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            consecutive_duplicates(123)
        with self.assertRaises(TypeError):
            consecutive_duplicates('123')
