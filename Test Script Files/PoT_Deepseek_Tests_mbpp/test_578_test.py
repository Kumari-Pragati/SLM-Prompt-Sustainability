import unittest
from mbpp_578_code import interleave_lists

class TestInterleaveLists(unittest.TestCase):

    def test_typical_case(self):
        list1 = [1, 2, 3]
        list2 = ['a', 'b', 'c']
        list3 = [True, False, True]
        expected_output = [1, 'a', True, 2, 'b', False, 3, 'c', True]
        self.assertEqual(interleave_lists(list1, list2, list3), expected_output)

    def test_empty_lists(self):
        list1 = []
        list2 = []
        list3 = []
        expected_output = []
        self.assertEqual(interleave_lists(list1, list2, list3), expected_output)

    def test_one_empty_list(self):
        list1 = [1, 2, 3]
        list2 = []
        list3 = [True, False, True]
        expected_output = [1, True]
        self.assertEqual(interleave_lists(list1, list2, list3), expected_output)

    def test_different_lengths(self):
        list1 = [1, 2, 3, 4]
        list2 = ['a', 'b', 'c']
        list3 = [True, False]
        expected_output = [1, 'a', True, 2, 'b', False, 3, 'c', 4]
        self.assertEqual(interleave_lists(list1, list2, list3), expected_output)

    def test_invalid_input(self):
        list1 = [1, 2, 3]
        list2 = ['a', 'b', 'c']
        list3 = 'not a list'
        with self.assertRaises(TypeError):
            interleave_lists(list1, list2, list3)
