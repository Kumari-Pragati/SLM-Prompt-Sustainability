import unittest
from mbpp_277_code import dict_filter

class TestDictFilter(unittest.TestCase):

    def test_dict_filter(self):
        # Test case 1: Filter dictionary with all values greater than or equal to 5
        dict1 = {'a': 1, 'b': 2, 'c': 5, 'd': 6, 'e': 7}
        result = dict_filter(dict1, 5)
        self.assertEqual(result, {'c': 5, 'd': 6, 'e': 7})

        # Test case 2: Filter dictionary with no values greater than or equal to 5
        dict2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        result = dict_filter(dict2, 5)
        self.assertEqual(result, {})

        # Test case 3: Filter dictionary with all values less than 5
        dict3 = {'a': 6, 'b': 7, 'c': 8, 'd': 9}
        result = dict_filter(dict3, 5)
        self.assertEqual(result, {'a': 6, 'b': 7, 'c': 8, 'd': 9})

        # Test case 4: Filter dictionary with mixed values
        dict4 = {'a': 1, 'b': 2, 'c': 5, 'd': 6, 'e': 7, 'f': 3}
        result = dict_filter(dict4, 5)
        self.assertEqual(result, {'c': 5, 'd': 6, 'e': 7})
