import unittest
from mbpp_757_code import count_reverse_pairs

class TestCountReversePairs(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_reverse_pairs([]), '0')

    def test_single_element(self):
        for test_str in ['abc', '123', 'Hello', 'True', 'False']:
            self.assertEqual(count_reverse_pairs([test_str]), '0')

    def test_simple_list(self):
        test_list = ['12', '34', '56', '78']
        expected_result = '2'
        self.assertEqual(count_reverse_pairs(test_list), expected_result)

    def test_reverse_pairs(self):
        test_list = ['12', '21', '34', '43', '56', '65']
        expected_result = '3'
        self.assertEqual(count_reverse_pairs(test_list), expected_result)

    def test_mixed_list(self):
        test_list = ['abc', '123', 'xyz', '456', '789', 'True', 'False']
        expected_result = '3'
        self.assertEqual(count_reverse_pairs(test_list), expected_result)

    def test_duplicates(self):
        test_list = ['12', '12', '34', '56', '56']
        expected_result = '1'
        self.assertEqual(count_reverse_pairs(test_list), expected_result)

    def test_long_list(self):
        test_list = [str(i) for i in range(100)]
        expected_result = str(sum([1 for i in range(0, len(test_list) - 1) for j in range(i + 1, len(test_list)): test_list[i] == test_list[j][::-1]]) if len(test_list) > 1 else '0')
        self.assertEqual(count_reverse_pairs(test_list), expected_result)

    def test_non_string_elements(self):
        test_list = [12, 'abc', 3.14, True, False]
        self.assertRaises(TypeError, count_reverse_pairs, test_list)
