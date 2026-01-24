import unittest
from mbpp_763_code import find_Min_Diff

class TestFindMinDiff(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 5), 0)
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6], 6), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Min_Diff([1], 1), 0)

    def test_edge_case_two_elements(self):
        self.assertEqual(find_Min_Diff([1, 2], 2), 0)

    def test_edge_case_duplicate_elements(self):
        self.assertEqual(find_Min_Diff([1, 1, 2], 3), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(find_Min_Diff([], 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(find_Min_Diff([-1, -2, -3, -4, -5], 5), 1)

    def test_large_numbers(self):
        self.assertEqual(find_Min_Diff([1000000001, 1000000002, 1000000003, 1000000004, 1000000005], 5), 1)

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            find_Min_Diff([1, 2, 3], 0)

    def test_invalid_input_list(self):
        with self.assertRaises(TypeError):
            find_Min_Diff('1, 2, 3', 3)
