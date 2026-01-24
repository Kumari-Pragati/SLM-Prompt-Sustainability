import unittest
from mbpp_316_code import find_last_occurrence

class TestFindLastOccurrence(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 4), 3)
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 1), 0)

    def test_edge(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 0), -1)
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(find_last_occurrence([], 1), -1)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            find_last_occurrence("abc", 1)
        with self.assertRaises(TypeError):
            find_last_occurrence([1, 2, 3], "a")
