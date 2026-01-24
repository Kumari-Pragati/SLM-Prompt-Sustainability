import unittest
from mbpp_567_code import issort_list

class TestIssortList(unittest.TestCase):
    def test_sorted_list(self):
        self.assertTrue(issort_list([1, 2, 3, 4, 5]))
        self.assertTrue(issort_list([0, 1, 2, 3, 4]))
        self.assertTrue(issort_list([-1, -2, -3, -4, -5]))

    def test_reverse_list(self):
        self.assertFalse(issort_list([5, 4, 3, 2, 1]))
        self.assertFalse(issort_list([4, 3, 2, 1, 0]))
        self.assertFalse(issort_list([-5, -4, -3, -2, -1]))

    def test_single_element(self):
        self.assertTrue(issort_list([1]))
        self.assertTrue(issort_list([]))

    def test_duplicates(self):
        self.assertTrue(issort_list([1, 1, 2, 3]))
        self.assertTrue(issort_list([1, 1, 1, 2]))
        self.assertTrue(issort_list([2, 2, 3, 4]))

    def test_empty_list_raise_exception(self):
        self.assertRaises(TypeError, issort_list, [])
