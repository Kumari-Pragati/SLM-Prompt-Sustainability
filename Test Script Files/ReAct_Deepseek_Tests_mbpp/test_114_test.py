import unittest
from mbpp_114_code import assign_freq

class TestAssignFreq(unittest.TestCase):

    def test_typical_case(self):
        test_list = [1, 2, 2, 3, 3, 3]
        expected_output = "[('1',), ('2', 2), ('3', 3)]"
        self.assertEqual(assign_freq(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = "[]"
        self.assertEqual(assign_freq(test_list), expected_output)

    def test_single_element(self):
        test_list = [1]
        expected_output = "[('1', 1)]"
        self.assertEqual(assign_freq(test_list), expected_output)

    def test_duplicate_elements(self):
        test_list = [1, 1, 1, 2, 2, 3]
        expected_output = "[('1', 3), ('2', 2), ('3', 1)]"
        self.assertEqual(assign_freq(test_list), expected_output)

    def test_string_elements(self):
        test_list = ['a', 'b', 'b', 'c', 'c', 'c']
        expected_output = "[('a', 1), ('b', 2), ('c', 3)]"
        self.assertEqual(assign_freq(test_list), expected_output)

    def test_mixed_elements(self):
        test_list = [1, 'a', 'a', 2, 2, 'c']
        expected_output = "[('1', 1), ('a', 2), ('2', 2), ('c', 1)]"
        self.assertEqual(assign_freq(test_list), expected_output)
