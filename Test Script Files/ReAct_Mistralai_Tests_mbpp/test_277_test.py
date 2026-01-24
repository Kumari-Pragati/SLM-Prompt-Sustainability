import unittest
from mbpp_277_code import dict_filter

class TestDictFilter(unittest.TestCase):

    def test_empty_dict(self):
        """Test filtering an empty dictionary"""
        result = dict_filter({}, 10)
        self.assertDictEqual(result, {})

    def test_single_item(self):
        """Test filtering a single item dictionary"""
        result = dict_filter({'key1': 5}, 5)
        self.assertDictEqual(result, {'key1': 5})

    def test_multiple_items(self):
        """Test filtering a multiple items dictionary"""
        result = dict_filter({'key1': 3, 'key2': 7, 'key3': 1}, 5)
        self.assertDictEqual(result, {'key2': 7})

    def test_boundary_case_zero(self):
        """Test filtering a dictionary with values equal to the threshold"""
        result = dict_filter({'key1': 0, 'key2': 0}, 0)
        self.assertDictEqual(result, {'key1': 0, 'key2': 0})

    def test_boundary_case_one_below(self):
        """Test filtering a dictionary with values just below the threshold"""
        result = dict_filter({'key1': 4, 'key2': 4}, 5)
        self.assertDictEqual(result, {})

    def test_negative_threshold(self):
        """Test filtering with a negative threshold"""
        with self.assertRaises(ValueError):
            dict_filter({'key1': 10, 'key2': 20}, -1)
