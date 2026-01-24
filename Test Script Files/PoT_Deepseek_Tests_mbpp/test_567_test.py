import unittest
from mbpp_567_code import issort_list

class TestIsSortList(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(issort_list([1, 2, 3, 4, 5]))
        self.assertTrue(issort_list([1, 2, 3, 4, 5, 6]))
        self.assertTrue(issort_list([1, 2, 3, 4, 5, 6, 7]))

    def test_edge_cases(self):
        self.assertTrue(issort_list([1]))
        self.assertTrue(issort_list([1, 2]))
        self.assertTrue(issort_list([1, 2, 3]))

    def test_boundary_conditions(self):
        self.assertTrue(issort_list([]))
        self.assertFalse(issort_list([3, 2, 1]))
        self.assertFalse(issort_list([5, 4, 3, 2, 1]))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            issort_list(None)
        with self.assertRaises(TypeError):
            issort_list('1,2,3,4,5')
        with self.assertRaises(TypeError):
            issort_list([1, '2', 3, 4, 5])
