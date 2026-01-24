import unittest
from mbpp_733_code import find_first_occurrence

class TestFindFirstOccurrence(unittest.TestCase):

    def test_find_first_occurrence(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 2), 1)
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(find_first_occurrence([1, 2, 2, 2, 3], 2), 1)
        self.assertEqual(find_first_occurrence([1, 2, 2, 2, 3], 1), 0)
        self.assertEqual(find_first_occurrence([1, 2, 2, 2, 3], 3), 4)
        self.assertEqual(find_first_occurrence([1, 1, 1, 1, 1], 1), 0)
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 0), -1)
