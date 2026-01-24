import unittest
from mbpp_567_code import issort_list

class TestIssortList(unittest.TestCase):
    def test_sorted_list(self):
        self.assertTrue(issort_list([1, 2, 3, 4, 5]))
        self.assertTrue(issort_list([0]))
        self.assertTrue(issort_list([-10, -9, -8, -7, -6]))

    def test_reversed_list(self):
        self.assertFalse(issort_list([5, 4, 3, 2, 1]))
        self.assertFalse(issort_list([10, 9, 8, 7, 6, 5]))
        self.assertFalse(issort_list([20, 19, 18, 17, 16, 15, 14]))

    def test_single_element_list(self):
        self.assertTrue(issort_list([1]))
        self.assertTrue(issort_list([-1]))
        self.assertTrue(issort_list([0]))

    def test_empty_list(self):
        self.assertTrue(issort_list([]))

    def test_duplicates(self):
        self.assertTrue(issort_list([1, 1, 2, 3, 4]))
        self.assertTrue(issort_list([-1, -1, -2, -3, -4]))
        self.assertTrue(issort_list([0, 0, 1, 2, 3]))

    def test_mixed_types(self):
        self.assertRaises(TypeError, issort_list, [1, 'a', 2])
        self.assertRaises(TypeError, issort_list, ['a', 1, 'b'])
        self.assertRaises(TypeError, issort_list, [1, 2, 3, 'a'])
