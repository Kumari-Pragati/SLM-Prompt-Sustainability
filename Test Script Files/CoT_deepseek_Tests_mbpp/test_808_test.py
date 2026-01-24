import unittest
from mbpp_808_code import check_K

class TestCheckK(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_K((1, 2, 3, 4, 5), 3))

    def test_edge_case(self):
        self.assertFalse(check_K((1, 2, 3, 4, 5), 6))

    def test_empty_tuple(self):
        self.assertFalse(check_K((), 1))

    def test_single_element_tuple(self):
        self.assertTrue(check_K((1,), 1))
        self.assertFalse(check_K((1,), 2))

    def test_duplicate_elements(self):
        self.assertTrue(check_K((1, 2, 3, 2, 1), 2))

    def test_large_tuple(self):
        self.assertTrue(check_K(tuple(range(1, 10000)), 5000))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_K("not a tuple", 1)
