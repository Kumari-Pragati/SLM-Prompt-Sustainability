import unittest
from mbpp_197_code import find_exponentio

class TestFindExponentio(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_exponentio((2, 3), (4, 5)), ((2**4, 3**5)))

    def test_edge_cases(self):
        self.assertEqual(find_exponentio((0, 1), (0, 0)), ((0**0, 1**0)))

    def test_boundary_cases(self):
        self.assertEqual(find_exponentio((1, -1), (0, -1)), ((1**0, -1**-1)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_exponentio((2, 3), 4)
