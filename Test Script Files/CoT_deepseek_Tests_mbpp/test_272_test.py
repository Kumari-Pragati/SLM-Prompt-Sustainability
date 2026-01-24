import unittest
from mbpp_272_code import rear_extract

class TestRearExtract(unittest.TestCase):

    def test_typical_case(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = [3, 6, 9]
        self.assertEqual(rear_extract(test_list), expected_output)

    def test_single_element(self):
        test_list = [[1]]
        expected_output = [1]
        self.assertEqual(rear_extract(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = []
        self.assertEqual(rear_extract(test_list), expected_output)

    def test_empty_sublists(self):
        test_list = [[]]
        expected_output = []
        self.assertEqual(rear_extract(test_list), expected_output)

    def test_negative_numbers(self):
        test_list = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        expected_output = [-3, -6, -9]
        self.assertEqual(rear_extract(test_list), expected_output)

    def test_mixed_types(self):
        test_list = [['a', 'b', 'c'], [1, 2, 3], [True, False, True]]
        expected_output = ['c', 3, True]
        self.assertEqual(rear_extract(test_list), expected_output)

    def test_empty_sublists_with_elements(self):
        test_list = [['a', 'b', 'c'], [], ['d', 'e', 'f']]
        expected_output = ['c', 'f']
        self.assertEqual(rear_extract(test_list), expected_output)
