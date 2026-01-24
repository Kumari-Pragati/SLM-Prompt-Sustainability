import unittest
from mbpp_227_code import min_of_three

class TestMinOfThree(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_of_three(1, 2, 3), 1)

    def test_edge_case(self):
        self.assertEqual(min_of_three(10, 10, 10), 10)

    def test_boundary_case(self):
        self.assertEqual(min_of_three(-1000, 0, 1000), -1000)
        self.assertEqual(min_of_three(float('-inf'), 0, float('inf')), float('-inf'))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_of_three("a", "b", "c")
        with self.assertRaises(TypeError):
            min_of_three(1, [1, 2, 3], 3)
        with self.assertRaises(TypeError):
            min_of_three(1, None, 3)
