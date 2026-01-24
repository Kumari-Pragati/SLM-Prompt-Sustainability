import unittest
from mbpp_197_code import find_exponentio

class TestFindExponentio(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_exponentio((2, 3, 4), (5, 6, 7)), (32, 729, 134217728))

    def test_edge_case(self):
        self.assertEqual(find_exponentio((0, 1), (0, 1)), (1, 1))

    def test_boundary_case(self):
        self.assertEqual(find_exponentio((1, 2, 3, 4, 5), (0, 1, 2, 3, 4)), (1, 2, 4, 8, 16))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_exponentio((1, 2, 3), 'a')
