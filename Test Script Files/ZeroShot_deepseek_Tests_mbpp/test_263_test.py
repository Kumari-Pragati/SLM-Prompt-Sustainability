import unittest
from mbpp_263_code import merge_dict

class TestMergeDict(unittest.TestCase):

    def test_merge_dict(self):
        # Test case 1: Merge two dictionaries with different keys
        d1 = {'a': 1, 'b': 2}
        d2 = {'c': 3, 'd': 4}
        expected_output = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        self.assertEqual(merge_dict(d1, d2), expected_output)

        # Test case 2: Merge two dictionaries with some common keys
        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'b': 4, 'd': 5, 'e': 6}
        expected_output = {'a': 1, 'b': 4, 'c': 3, 'd': 5, 'e': 6}
        self.assertEqual(merge_dict(d1, d2), expected_output)

        # Test case 3: Merge two empty dictionaries
        d1 = {}
        d2 = {}
        expected_output = {}
        self.assertEqual(merge_dict(d1, d2), expected_output)

        # Test case 4: Merge two dictionaries with one empty
        d1 = {'a': 1, 'b': 2}
        d2 = {}
        expected_output = {'a': 1, 'b': 2}
        self.assertEqual(merge_dict(d1, d2), expected_output)

        # Test case 5: Merge two dictionaries with one having None values
        d1 = {'a': None, 'b': 2}
        d2 = {'c': 3, 'd': 4}
        expected_output = {'a': None, 'b': 2, 'c': 3, 'd': 4}
        self.assertEqual(merge_dict(d1, d2), expected_output)
