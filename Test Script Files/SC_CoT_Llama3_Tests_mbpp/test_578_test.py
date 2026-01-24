import unittest
from mbpp_578_code import interleave_lists

class TestInterleaveLists(unittest.TestCase):

    def test_typical_inputs(self):
        list1 = [1, 2, 3]
        list2 = ['a', 'b', 'c']
        list3 = [4, 5, 6]
        result = interleave_lists(list1, list2, list3)
        self.assertEqual(result, [1, 'a', 4, 2, 'b', 5, 3, 'c', 6])

    def test_empty_lists(self):
        list1 = []
        list2 = []
        list3 = []
        result = interleave_lists(list1, list2, list3)
        self.assertEqual(result, [])

    def test_lists_of_different_lengths(self):
        list1 = [1, 2, 3, 4]
        list2 = ['a', 'b', 'c']
        list3 = [4, 5, 6, 7, 8]
        result = interleave_lists(list1, list2, list3)
        self.assertEqual(result, [1, 'a', 4, 2, 'b', 5, 3, 'c', 6, 7, 8])

    def test_lists_of_zero_length(self):
        list1 = []
        list2 = []
        list3 = []
        result = interleave_lists(list1, list2, list3)
        self.assertEqual(result, [])

    def test_lists_of_one_element(self):
        list1 = [1]
        list2 = ['a']
        list3 = [4]
        result = interleave_lists(list1, list2, list3)
        self.assertEqual(result, [1, 'a', 4])

    def test_lists_of_two_elements(self):
        list1 = [1, 2]
        list2 = ['a', 'b']
        list3 = [4, 5]
        result = interleave_lists(list1, list2, list3)
        self.assertEqual(result, [1, 'a', 4, 2, 'b', 5])
