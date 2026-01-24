import unittest
from mbpp_808_code import check_K

class TestCheckK(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(check_K((1, 2, 3, 4, 5), 3))

    def test_edge_condition(self):
        self.assertTrue(check_K((1,), 1))

    def test_boundary_condition(self):
        self.assertFalse(check_K((1, 2, 3, 4, 5), 6))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_K("1, 2, 3, 4, 5", 1)

    def test_empty_tuple(self):
        self.assertFalse(check_K((), 1))
