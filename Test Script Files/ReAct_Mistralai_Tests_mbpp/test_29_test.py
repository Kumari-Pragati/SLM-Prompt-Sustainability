import unittest
from29_code import get_Odd_Occurrence

class TestGetOddOccurrence(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(get_Odd_Occurrence([], 0), -1)

    def test_single_element_array(self):
        for element in [1, 2, 3, 4, 5]:
            self.assertEqual(get_Odd_Occurrence([element], 1), element)
            self.assertEqual(get_Odd_Occurrence([element], 2), -1)

    def test_single_occurrence(self):
        arr = [1, 2, 3, 2, 2, 4, 4, 5]
        self.assertEqual(get_Odd_Occurrence(arr, len(arr)), 1)

    def test_multiple_occurrences(self):
        arr = [1, 2, 3, 2, 2, 4, 4, 5]
        self.assertNotEqual(get_Odd_Occurrence(arr, len(arr)), 2)
        self.assertNotEqual(get_Odd_Occurrence(arr, len(arr)), 4)

    def test_duplicate_first_element(self):
        arr = [1, 1, 3, 2, 2, 4, 4, 5]
        self.assertEqual(get_Odd_Occurrence(arr, len(arr)), 3)

    def test_duplicate_last_element(self):
        arr = [1, 3, 3, 2, 2, 4, 4, 4]
        self.assertEqual(get_Odd_Occurrence(arr, len(arr)), 1)

    def test_all_same_element(self):
        arr = [1, 1, 1, 1, 1, 1]
        self.assertEqual(get_Odd_Occurrence(arr, len(arr)), -1)

    def test_negative_elements(self):
        arr = [-1, -2, -3, -2, -2, 4, 4, 5]
        self.assertEqual(get_Odd_Occurrence(arr, len(arr)), -3)
