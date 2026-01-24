import unittest
from mbpp_62_code import smallest_num

class TestSmallestNum(unittest.TestCase):

    def test_empty_list(self):
        """Tests smallest_num with an empty list"""
        self.assertIsNone(smallest_num([]))

    def test_single_element(self):
        """Tests smallest_num with a single element list"""
        self.assertEqual(smallest_num([42]), 42)

    def test_multiple_elements(self):
        """Tests smallest_num with multiple elements list"""
        self.assertEqual(smallest_num([1, 2, 3, 4]), 1)

    def test_duplicates(self):
        """Tests smallest_num with duplicate elements"""
        self.assertEqual(smallest_num([1, 1, 2, 3]), 1)

    def test_negative_numbers(self):
        """Tests smallest_num with negative numbers"""
        self.assertEqual(smallest_num([-1, -2, -3]), -3)

    def test_mixed_numbers(self):
        """Tests smallest_num with mixed numbers"""
        self.assertEqual(smallest_num([-1, 0, 1, 2]), -1)

    def test_large_numbers(self):
        """Tests smallest_num with large numbers"""
        self.assertEqual(smallest_num([1000000001, 1000000002, 1000000003]), 1000000001)

    def test_floats(self):
        """Tests smallest_num with floats"""
        self.assertAlmostEqual(smallest_num([3.14, 2.71, 1.618]), 1.618)

    def test_list_with_none(self):
        """Tests smallest_num with a list containing None"""
        self.assertIsNone(smallest_num([None, 1, 2, 3]))
