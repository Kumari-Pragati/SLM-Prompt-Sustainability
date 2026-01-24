import unittest
from mbpp_695_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_greater((1, 2), (1, 2)))

    def test_edge_case_equal(self):
        self.assertFalse(check_greater((1, 1), (1, 1)))

    def test_edge_case_reverse(self):
        self.assertFalse(check_greater((2, 1), (1, 2)))

    def test_edge_case_empty(self):
        with self.assertRaises(TypeError):
            check_greater([], [])

    def test_edge_case_single(self):
        self.assertTrue(check_greater((1,), (1,)))

    def test_edge_case_single_reverse(self):
        self.assertFalse(check_greater((1,), (1,)))

    def test_edge_case_single_empty(self):
        with self.assertRaises(TypeError):
            check_greater((1,), [])

    def test_edge_case_empty_single(self):
        with self.assertRaises(TypeError):
            check_greater([], (1,))

    def test_edge_case_empty_single_reverse(self):
        with self.assertRaises(TypeError):
            check_greater([], (1,))
