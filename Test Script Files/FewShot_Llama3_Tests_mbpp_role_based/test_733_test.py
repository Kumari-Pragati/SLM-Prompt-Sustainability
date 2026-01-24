import unittest
from mbpp_733_code import find_first_occurrence

class TestFindFirstOccurrence(unittest.TestCase):
    def test_found_at_start(self):
        A = [1, 2, 3, 4, 5]
        x = 1
        self.assertEqual(find_first_occurrence(A, x), 0)

    def test_found_at_end(self):
        A = [1, 2, 3, 4, 5]
        x = 5
        self.assertEqual(find_first_occurrence(A, x), 4)

    def test_found_in_middle(self):
        A = [1, 2, 3, 4, 5]
        x = 3
        self.assertEqual(find_first_occurrence(A, x), 2)

    def test_not_found(self):
        A = [1, 2, 3, 4, 5]
        x = 6
        self.assertEqual(find_first_occurrence(A, x), -1)

    def test_empty_array(self):
        A = []
        x = 1
        self.assertEqual(find_first_occurrence(A, x), -1)

    def test_single_element_array(self):
        A = [1]
        x = 1
        self.assertEqual(find_first_occurrence(A, x), 0)

    def test_array_with_duplicates(self):
        A = [1, 2, 2, 3, 4, 5]
        x = 2
        self.assertEqual(find_first_occurrence(A, x), 1)
