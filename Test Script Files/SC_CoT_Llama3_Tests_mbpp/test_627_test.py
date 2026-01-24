import unittest
from mbpp_627_code import find_First_Missing

class TestFindFirstMissing(unittest.TestCase):
    def test_typical_input(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(find_First_Missing(array, 0, 10), 11)

    def test_edge_case_start_equal_end(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(find_First_Missing(array, 0, 9), 10)

    def test_edge_case_start_greater_than_end(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(find_First_Missing(array, 10, 0), 1)

    def test_edge_case_array_contains_duplicates(self):
        array = [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(find_First_Missing(array, 0, 9), 10)

    def test_edge_case_array_missing_single_element(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
        self.assertEqual(find_First_Missing(array, 0, 10), 10)

    def test_edge_case_array_missing_multiple_elements(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13]
        self.assertEqual(find_First_Missing(array, 0, 13), 11)

    def test_edge_case_array_missing_elements_at_start(self):
        array = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(find_First_Missing(array, 0, 12), 1)

    def test_edge_case_array_missing_elements_at_end(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(find_First_Missing(array, 0, 10), 11)

    def test_invalid_input_array_length_zero(self):
        array = []
        with self.assertRaises(IndexError):
            find_First_Missing(array, 0, 0)

    def test_invalid_input_array_length_one(self):
        array = [0]
        with self.assertRaises(IndexError):
            find_First_Missing(array, 0, 0)
