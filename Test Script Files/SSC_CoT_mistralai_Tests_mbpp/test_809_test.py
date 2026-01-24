import unittest
from mbpp_809_code import check_smaller

class TestCheckSmaller(unittest.TestCase):

    def test_normal_case(self):
        self.assertTrue(check_smaller((1, 2, 3), (2, 3, 4)))
        self.assertTrue(check_smaller((5, 4, 3), (5, 4, 2)))

    def test_edge_case_equal_elements(self):
        self.assertTrue(check_smaller((1, 1, 2), (1, 1, 2)))
        self.assertFalse(check_smaller((1, 1, 2), (1, 2, 2)))

    def test_edge_case_one_smaller(self):
        self.assertFalse(check_smaller((1, 2, 3), (1, 2, 3)))
        self.assertTrue(check_smaller((1, 2, 3), (2, 2, 3)))
        self.assertTrue(check_smaller((1, 2, 3), (1, 3, 3)))

    def test_edge_case_one_larger(self):
        self.assertFalse(check_smaller((2, 2, 3), (1, 2, 3)))
        self.assertFalse(check_smaller((2, 2, 3), (1, 2, 4)))
        self.assertFalse(check_smaller((2, 2, 3), (1, 3, 4)))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, check_smaller, (1, 2), '3')
        self.assertRaises(TypeError, check_smaller, [1, 2], [3, 4, 5])
