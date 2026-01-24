import unittest
from mbpp_418_code import Find_Max

class TestFindMax(unittest.TestCase):

    def test_empty_list(self):
        """Test finding max on an empty list"""
        self.assertIsNone(Find_Max([]))

    def test_single_element_list(self):
        """Test finding max on a list with one element"""
        self.assertEqual(Find_Max([1]), 1)

    def test_multiple_elements_list(self):
        """Test finding max on a list with multiple elements"""
        self.assertEqual(Find_Max([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers_list(self):
        """Test finding max on a list with negative numbers"""
        self.assertEqual(Find_Max([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers_list(self):
        """Test finding max on a list with mixed numbers"""
        self.assertEqual(Find_Max([1, -2, 3, -4, 5]), 5)

    def test_duplicate_numbers_list(self):
        """Test finding max on a list with duplicate numbers"""
        self.assertEqual(Find_Max([1, 1, 2, 1, 3]), 3)

    def test_list_with_zero(self):
        """Test finding max on a list with zero"""
        self.assertEqual(Find_Max([0, 1, 2, 3, 4]), 4)

    def test_list_with_float(self):
        """Test finding max on a list with floats"""
        self.assertEqual(Find_Max([1.1, 2.2, 3.3]), 3.3)

    def test_list_with_strings(self):
        """Test finding max on a list with strings"""
        self.assertEqual(Find_Max(["a", "b", "c"]), "c")
