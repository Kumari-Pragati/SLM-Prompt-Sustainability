import unittest
from mbpp_760_code import unique_Element

class TestUniqueElement(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(unique_Element(arr, n), 'YES')

    def test_typical_case_with_duplicates(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(unique_Element(arr, n), 'YES')

    def test_edge_case_single_element(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(unique_Element(arr, n), 'YES')

    def test_edge_case_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(unique_Element(arr, n), 'YES')

    def test_edge_case_all_same_elements(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(unique_Element(arr, n), 'YES')

    def test_typical_case_with_different_elements(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(unique_Element(arr, n), 'YES')

    def test_edge_case_negative_numbers(self):
        arr = [-1, -1, -1, -1, -1]
        n = len(arr)
        self.assertEqual(unique_Element(arr, n), 'YES')

    def test_edge_case_mixed_numbers(self):
        arr = [1, -1, 2, -2, 3]
        n = len(arr)
        self.assertEqual(unique_Element(arr, n), 'YES')

    def test_typical_case_with_duplicates_and_different_elements(self):
        arr = [1, 2, 2, 3, 4]
        n = len(arr)
        self.assertEqual(unique_Element(arr, n), 'NO')
