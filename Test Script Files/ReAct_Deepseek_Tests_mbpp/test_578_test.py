import unittest
from mbpp_578_code import interleave_lists

class TestInterleaveLists(unittest.TestCase):

    def test_typical_case(self):
        list1 = [1, 2, 3]
        list2 = ['a', 'b', 'c']
        list3 = [True, False, True]
        expected_result = [1, 'a', True, 2, 'b', False, 3, 'c', True]
        self.assertEqual(interleave_lists(list1, list2, list3), expected_result)

    def test_empty_lists(self):
        list1 = []
        list2 = []
        list3 = []
        expected_result = []
        self.assertEqual(interleave_lists(list1, list2, list3), expected_result)

    def test_different_length_lists(self):
        list1 = [1, 2, 3, 4]
        list2 = ['a', 'b', 'c']
        list3 = [True, False]
        expected_result = [1, 'a', True, 2, 'b', False, 3, 'c', 4, True, False]
        self.assertEqual(interleave_lists(list1, list2, list3), expected_result)

    def test_single_element_lists(self):
        list1 = [1]
        list2 = ['a']
        list3 = [True]
        expected_result = [1, 'a', True]
        self.assertEqual(interleave_lists(list1, list2, list3), expected_result)
