import unittest
from mbpp_197_code import find_exponentio

class TestFindExponentio(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_exponentio((2, 3), (4, 5)), (16, 243))

    def test_edge_condition(self):
        self.assertEqual(find_exponentio((0, 0), (0, 0)), (0, 0))

    def test_boundary_condition(self):
        self.assertEqual(find_exponentio((1, 2), (3, 4)), (1, 16))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_exponentio((1, 2), '3', 4)
