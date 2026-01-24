import unittest
from mbpp_424_code import extract_rear

class TestExtractRear(unittest.TestCase):

    def test_typical_case(self):
        test_tuple = (['a', 'b', 'c'], [1, 2, 3], ['x', 'y', 'z'])
        expected_output = ['c', 3, 'z']
        self.assertEqual(extract_rear(test_tuple), expected_output)

    def test_empty_list(self):
        test_tuple = ([], [], [])
        expected_output = []
        self.assertEqual(extract_rear(test_tuple), expected_output)

    def test_single_element(self):
        test_tuple = (['a'], [1], ['x'])
        expected_output = ['a', 1, 'x']
        self.assertEqual(extract_rear(test_tuple), expected_output)

    def test_none_in_tuple(self):
        test_tuple = (None, ['b', 'c'], None)
        with self.assertRaises(TypeError):
            extract_rear(test_tuple)

    def test_non_list_in_tuple(self):
        test_tuple = ('a', 'b', 'c')
        with self.assertRaises(TypeError):
            extract_rear(test_tuple)
