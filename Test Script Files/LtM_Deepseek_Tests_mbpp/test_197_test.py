import unittest
from mbpp_197_code import find_exponentio

class TestFindExponentio(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_exponentio((2, 3), (4, 5)), ((2**4, 3**5)))

    def test_edge_conditions(self):
        self.assertEqual(find_exponentio((0, 0), (1, 1)), ((0**1, 0**1)))
        self.assertEqual(find_exponentio((2, 3), (0, 0)), ((2**0, 3**0)))

    def test_boundary_conditions(self):
        self.assertEqual(find_exponentio((2, 3), (1000, 1000)), ((2**1000, 3**1000)))
        self.assertEqual(find_exponentio((-2, 3), (2, 3)), ((-2**2, 3**3)))

    def test_complex_cases(self):
        self.assertEqual(find_exponentio((2, 3), (2, 3)), ((2**2, 3**3)))
        self.assertEqual(find_exponentio((-2, -3), (2, 3)), ((-2**2, -3**3)))
