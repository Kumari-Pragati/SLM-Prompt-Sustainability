import unittest
from mbpp_924_code import max_of_two

class TestMaxOfTwo(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_of_two(5, 10), 10)

    def test_boundary_conditions(self):
        self.assertEqual(max_of_two(0, 0), 0)
        self.assertEqual(max_of_two(-10, -5), -5)

    def test_edge_cases(self):
        self.assertEqual(max_of_two(float('inf'), float('inf')), float('inf'))
        self.assertEqual(max_of_two(float('-inf'), float('-inf')), float('-inf'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            max_of_two("5", 10)
        with self.assertRaises(TypeError):
            max_of_two(5, "10")
        with self.assertRaises(TypeError):
            max_of_two("5", "10")
