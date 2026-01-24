import unittest
from mbpp_216_code import check_subset_list

class TestCheckSubsetList(unittest.TestCase):

    def test_normal_input(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2]))
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2, 3]))
        self.assertTrue(check_subset_list([1, 2], [1, 2, 3]))

    def test_edge_cases(self):
        self.assertFalse(check_subset_list([1, 2], [1, 3]))
        self.assertFalse(check_subset_list([], [1]))
        self.assertFalse(check_subset_list([1], []))
        self.assertFalse(check_subset_list([1, 2, 3], []))
        self.assertFalse(check_subset_list([], []))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, check_subset_list, 'a', [1])
        self.assertRaises(TypeError, check_subset_list, [1], 'a')
