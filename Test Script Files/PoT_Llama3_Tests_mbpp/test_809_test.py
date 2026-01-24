import unittest
from mbpp_809_code import check_smaller

class TestCheckSmaller(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_smaller((1, 2, 3), (0, 1, 2)))

    def test_edge_case_equal(self):
        self.assertFalse(check_smaller((1, 1, 1), (1, 1, 1)))

    def test_edge_case_reverse(self):
        self.assertFalse(check_smaller((3, 2, 1), (1, 2, 3)))

    def test_edge_case_empty(self):
        with self.assertRaises(TypeError):
            check_smaller([], [])

    def test_edge_case_single(self):
        self.assertTrue(check_smaller((1,), (0,)))

    def test_edge_case_single_reverse(self):
        self.assertFalse(check_smaller((1,), (1,)))

    def test_edge_case_single_empty(self):
        with self.assertRaises(TypeError):
            check_smaller((1,), [])

    def test_edge_case_empty_single(self):
        with self.assertRaises(TypeError):
            check_smaller([], (1,))

    def test_edge_case_empty_single_reverse(self):
        with self.assertRaises(TypeError):
            check_smaller([], (1,))
