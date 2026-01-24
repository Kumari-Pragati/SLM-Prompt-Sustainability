import unittest
from mbpp_227_code import min_of_three

class TestMinOfThree(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_of_three(1, 2, 3), 1)

    def test_edge_case(self):
        self.assertEqual(min_of_three(0, -1, -2), -2)

    def test_boundary_case(self):
        self.assertEqual(min_of_three(float('inf'), float('inf'), float('inf')), float('inf'))

    def test_special_case(self):
        self.assertEqual(min_of_three(1.1, 1.2, 1.3), 1.1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_of_three("1", 2, 3)
