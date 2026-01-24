import unittest
from mbpp_418_code import Find_Max

class TestFindMax(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(Find_Max([]), None)

    def test_single_element_list(self):
        self.assertEqual(Find_Max([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(Find_Max([1, 2, 3, 4, 5]), 5)

    def test_duplicate_elements_list(self):
        self.assertEqual(Find_Max([1, 1, 2, 1, 3, 1, 4, 1, 5]), 5)

    def test_negative_numbers_list(self):
        self.assertEqual(Find_Max([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers_list(self):
        self.assertEqual(Find_Max([1, -2, 3, -4, 5]), 5)

    def test_list_with_zero(self):
        self.assertEqual(Find_Max([0, 1, 2, 3, 4, 5]), 5)

    def test_list_with_float(self):
        self.assertEqual(Find_Max([1.1, 2.2, 3.3, 4.4, 5.5]), 5.5)

    def test_list_with_strings(self):
        self.assertEqual(Find_Max(["a", "b", "c", "d", "e"]), None)

    def test_list_with_mixed_types(self):
        self.assertEqual(Find_Max([1, "a", 2, "b", 3, "c", 4, "d", 5]), None)
