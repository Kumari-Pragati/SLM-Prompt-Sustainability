import unittest
from mbpp_730_code import consecutive_duplicates

class TestConsecutiveDuplicates(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(consecutive_duplicates([1, 1, 2, 3, 4, 4, 5]), [1, 1, 4, 4])
        self.assertEqual(consecutive_duplicates([1, 1, 1, 2, 3, 4, 4, 5]), [1, 1, 1, 2, 4, 4])
        self.assertEqual(consecutive_duplicates([1, 2, 2, 3, 4, 4, 5]), [1, 2, 2, 3, 4, 4])

    def test_edge_cases(self):
        self.assertEqual(consecutive_duplicates([]), [])
        self.assertEqual(consecutive_duplicates([1]), [1])
        self.assertEqual(consecutive_duplicates([1, 1]), [1, 1])
        self.assertEqual(consecutive_duplicates([1, 1, 1]), [1, 1, 1])
        self.assertEqual(consecutive_duplicates([1, 1, 1, 1]), [1, 1, 1, 1])
        self.assertEqual(consecutive_duplicates([1, 1, 1, 2]), [1, 1, 1, 2])
        self.assertEqual(consecutive_duplicates([1, 1, 1, 1, 2]), [1, 1, 1, 1, 2])
        self.assertEqual(consecutive_duplicates([1, 1, 1, 1, 1, 2]), [1, 1, 1, 1, 1, 2])

    def test_complex(self):
        self.assertEqual(consecutive_duplicates([1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2]), [1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2])
        self.assertEqual(consecutive_duplicates([1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1]), [1, 1, 1, 2, 1, 1, 1, 2, 1])
        self.assertEqual(consecutive_duplicates([1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1]), [1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2])
        self.assertEqual(consecutive_duplicates([1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1]), [1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2])
