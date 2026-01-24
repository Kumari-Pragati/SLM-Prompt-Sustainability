import unittest
from mbpp_161_code import remove_elements

class TestRemoveElements(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], [2, 4]), [1, 3, 5])

    def test_edge_case_empty_list1(self):
        self.assertEqual(remove_elements([], [2, 4]), [])

    def test_edge_case_empty_list2(self):
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], []), [1, 2, 3, 4, 5])

    def test_edge_case_list1_subset_of_list2(self):
        self.assertEqual(remove_elements([1, 2, 3], [1, 2, 3, 4, 5]), [])

    def test_edge_case_list2_subset_of_list1(self):
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], [1, 2, 3]), [4, 5])

    def test_edge_case_list1_subset_of_list2_and_list2_subset_of_list1(self):
        self.assertEqual(remove_elements([1, 2, 3], [1, 2, 3, 4, 5]), [])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            remove_elements('abc', [2, 4])

    def test_invalid_input_non_list2(self):
        with self.assertRaises(TypeError):
            remove_elements([1, 2, 3], 'abc')

    def test_invalid_input_non_list3(self):
        with self.assertRaises(TypeError):
            remove_elements('abc', 'def')
