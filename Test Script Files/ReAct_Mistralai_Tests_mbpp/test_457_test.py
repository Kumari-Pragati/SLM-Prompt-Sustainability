import unittest
from mbpp_457_code import Find_Min

class TestFindMin(unittest.TestCase):

    def test_empty_list(self):
        """Test Find_Min with an empty list"""
        self.assertIsNone(Find_Min([]))

    def test_single_element_list(self):
        """Test Find_Min with a list containing a single element"""
        self.assertEqual(Find_Min([1]), 1)

    def test_multiple_elements_list(self):
        """Test Find_Min with a list containing multiple elements"""
        self.assertEqual(Find_Min([1, 2, 3, 4, 5]), 1)

    def test_negative_numbers_list(self):
        """Test Find_Min with a list containing negative numbers"""
        self.assertEqual(Find_Min([-1, -2, -3, -4, -5]), -5)

    def test_mixed_numbers_list(self):
        """Test Find_Min with a list containing mixed numbers"""
        self.assertEqual(Find_Min([1, -2, 3, -4, 5]), -4)

    def test_floats_list(self):
        """Test Find_Min with a list containing floats"""
        self.assertAlmostEqual(Find_Min([1.1, 2.2, 3.3, 4.4, 5.5]), 1.1)

    def test_list_with_non_numeric_elements(self):
        """Test Find_Min with a list containing non-numeric elements"""
        self.assertRaises(TypeError, Find_Min, ['a', 1, 'b', 2, 'c'])
