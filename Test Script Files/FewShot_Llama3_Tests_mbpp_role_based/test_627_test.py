import unittest
from mbpp_627_code import find_First_Missing

class TestFindFirstMissing(unittest.TestCase):
    def test_typical_use_case(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
        self.assertEqual(find_First_Missing(array, 0, 10), 10)

    def test_edge_case_start_greater_than_end(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
        self.assertEqual(find_First_Missing(array, 10, 0), 1)

    def test_edge_case_array_with_duplicates(self):
        array = [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 11]
        self.assertEqual(find_First_Missing(array, 0, 11), 3)

    def test_edge_case_array_with_missing_element(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(find_First_Missing(array, 0, 10), 10)

    def test_invalid_input_array_length_zero(self):
        array = []
        with self.assertRaises(IndexError):
            find_First_Missing(array, 0, 0)

    def test_invalid_input_array_length_one(self):
        array = [0]
        with self.assertRaises(IndexError):
            find_First_Missing(array, 0, 0)
