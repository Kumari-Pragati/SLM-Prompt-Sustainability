import unittest
from mbpp_578_code import interleave_lists

class TestInterleaveLists(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = [1, 2, 3]
        list2 = ['a', 'b', 'c']
        list3 = ['x', 'y', 'z']
        expected_output = [1, 'a', 'x', 2, 'b', 'y', 3, 'c', 'z']
        self.assertEqual(interleave_lists(list1, list2, list3), expected_output)

    def test_empty_lists(self):
        list1 = []
        list2 = []
        list3 = []
        expected_output = []
        self.assertEqual(interleave_lists(list1, list2, list3), expected_output)

    def test_single_element_lists(self):
        list1 = [1]
        list2 = ['a']
        list3 = ['x']
        expected_output = [1, 'a', 'x']
        self.assertEqual(interleave_lists(list1, list2, list3), expected_output)

    def test_unequal_length_lists(self):
        list1 = [1, 2, 3]
        list2 = ['a', 'b']
        list3 = ['x']
        with self.assertRaises(ValueError):
            interleave_lists(list1, list2, list3)
