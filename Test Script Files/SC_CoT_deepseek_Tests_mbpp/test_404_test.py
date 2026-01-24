import unittest
from mbpp_404_code import minimum

class TestMinimum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(minimum(5, 10), 5)
        self.assertEqual(minimum(15, 10), 10)

    def test_edge_cases(self):
        self.assertEqual(minimum(0, 0), 0)
        self.assertEqual(minimum(-5, -10), -10)

    def test_boundary_conditions(self):
        self.assertEqual(minimum(float('inf'), float('inf')), float('inf'))
        self.assertEqual(minimum(float('-inf'), float('-inf')), float('-inf'))
        self.assertEqual(minimum(float('inf'), float('-inf')), float('-inf'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            minimum(5, 'a')
        with self.assertRaises(TypeError):
            minimum('a', 5)
        with self.assertRaises(TypeError):
            minimum('a', 'b')
