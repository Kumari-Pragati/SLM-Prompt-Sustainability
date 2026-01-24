import unittest
from mbpp_89_code import closest_num

class TestClosestNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(closest_num(10), 9)

    def test_boundary_case(self):
        self.assertEqual(closest_num(1), 0)

    def test_edge_case(self):
        self.assertEqual(closest_num(0), -1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            closest_num('a')
