import unittest
from mbpp_446_code import count_Occurrence

class TestCountOccurrence(unittest.TestCase):
    def test_typical_use_case(self):
        tup = (1, 2, 3)
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(count_Occurrence(tup, lst), 3)

    def test_empty_tuple(self):
        tup = ()
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(count_Occurrence(tup, lst), 0)

    def test_empty_list(self):
        tup = (1, 2, 3)
        lst = []
        self.assertEqual(count_Occurrence(tup, lst), 0)

    def test_no_occurrences(self):
        tup = (1, 2, 3)
        lst = [4, 5, 6]
        self.assertEqual(count_Occurrence(tup, lst), 0)

    def test_all_occurrences(self):
        tup = (1, 2, 3)
        lst = [1, 2, 3]
        self.assertEqual(count_Occurrence(tup, lst), 3)

    def test_duplicates(self):
        tup = (1, 2, 2)
        lst = [1, 2, 2, 3]
        self.assertEqual(count_Occurrence(tup, lst), 3)
