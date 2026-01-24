import unittest
from mbpp_695_code import check_greater

class TestCheckGreater(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(check_greater((1, 2, 3), (2, 3, 4)))

    def test_edge_case_equal(self):
        self.assertFalse(check_greater((1, 1, 1), (1, 1, 1)))

    def test_edge_case_reverse(self):
        self.assertTrue(check_greater((4, 3, 2), (2, 3, 4)))

    def test_edge_case_empty(self):
        with self.assertRaises(TypeError):
            check_greater([], [])

    def test_edge_case_single_element(self):
        self.assertTrue(check_greater((1,), (1,)))

    def test_edge_case_single_element_reverse(self):
        self.assertFalse(check_greater((1,), (1,)))

    def test_edge_case_single_element_empty(self):
        with self.assertRaises(TypeError):
            check_greater((1,), [])

    def test_edge_case_empty_reverse(self):
        with self.assertRaises(TypeError):
            check_greater([], (1,))
