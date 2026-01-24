import unittest
from mbpp_197_code import find_exponentio

class TestFindExponentio(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(find_exponentio((1, 2), (3, 4)), ((1**2, 1**3), (2**2, 2**3)))

    def test_edge_cases(self):
        self.assertEqual(find_exponentio((0, 0), (0, 0)), ((0, 0), (0, 0)))
        self.assertEqual(find_exponentio((1, 2), (0, 0)), ((1**0, 1**2), (2**0, 2**2)))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_exponentio('test', 'test')
        with self.assertRaises(TypeError):
            find_exponentio((1, 2), 'test')

    def test_boundary_cases(self):
        self.assertEqual(find_exponentio((-1, -2), (-3, -4)), ((-1**-2, (-1)**-3), (-2**-2, (-2)**-3))
        self.assertEqual(find_exponentio((1, 2), (3, 4)), ((1**2, 1**3), (2**2, 2**3)))
