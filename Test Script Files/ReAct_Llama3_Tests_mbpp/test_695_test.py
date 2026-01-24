import unittest
from mbpp_695_code import check_greater

class TestCheckGreater(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_greater((1, 2), (2, 3)))

    def test_edge_case_equal(self):
        self.assertFalse(check_greater((1, 1), (1, 1)))

    def test_edge_case_reverse(self):
        self.assertTrue(check_greater((2, 1), (1, 2)))

    def test_edge_case_empty(self):
        with self.assertRaises(TypeError):
            check_greater([], [])

    def test_edge_case_single_element(self):
        with self.assertRaises(TypeError):
            check_greater([1], [])

    def test_edge_case_mixed_types(self):
        with self.assertRaises(TypeError):
            check_greater([1, 'a'], [2, 'b'])

    def test_edge_case_mixed_types2(self):
        with self.assertRaises(TypeError):
            check_greater([1, 'a'], [2])
