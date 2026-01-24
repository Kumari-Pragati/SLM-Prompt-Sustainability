import unittest
from mbpp_808_code import check_K

class TestCheckK(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_K((1, 2, 3, 4, 5), 3))

    def test_edge_case(self):
        self.assertFalse(check_K((1, 2, 3, 4, 5), 6))

    def test_boundary_case(self):
        self.assertTrue(check_K((1, 2, 3, 4, 5), 1))
        self.assertTrue(check_K((1, 2, 3, 4, 5), 5))

    def test_special_case(self):
        self.assertTrue(check_K(('a', 'b', 'c', 'd', 'e'), 'c'))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_K((1, 2, 3, 4, 5), 'a')
