import unittest
from mbpp_59_code import is_octagonal

class TestIsOctagonal(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(is_octagonal(0), False)
        self.assertEqual(is_octagonal(1), False)
        self.assertEqual(is_octagonal(2), True)
        self.assertEqual(is_octagonal(3), True)
        self.assertEqual(is_octagonal(4), False)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(is_octagonal(-1), False)
        self.assertEqual(is_octagonal(0), False)
        self.assertEqual(is_octagonal(5), False)
        self.assertEqual(is_octagonal(10), True)
        self.assertEqual(is_octagonal(20), True)

    def test_complex_and_corner_cases(self):
        self.assertEqual(is_octagonal(-5), False)
        self.assertEqual(is_octagonal(-10), False)
        self.assertEqual(is_octagonal(15), True)
        self.assertEqual(is_octagonal(25), True)
