import unittest
from mbpp_970_code import min_of_two

class TestMinOfTwo(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_of_two(3, 5), 3)

    def test_boundary_condition(self):
        self.assertEqual(min_of_two(0, 0), 0)

    def test_edge_case(self):
        self.assertEqual(min_of_two(float('inf'), float('inf')), float('inf'))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_of_two("3", 5)
