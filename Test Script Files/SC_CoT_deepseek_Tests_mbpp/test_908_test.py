import unittest

from mbpp_908_code import find_fixed_point

class TestFindFixedPoint(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_fixed_point([0, 2, 5, 8, 17], 5), 0)

    def test_edge_case(self):
        self.assertEqual(find_fixed_point([-10, -5, 0, 3, 7], 5), 2)

    def test_boundary_case(self):
        self.assertEqual(find_fixed_point([], 0), -1)
        self.assertEqual(find_fixed_point([0], 1), 0)

    def test_special_case(self):
        self.assertEqual(find_fixed_point([10, 20, 30, 40], 4), -1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_fixed_point("not a list", 1)
