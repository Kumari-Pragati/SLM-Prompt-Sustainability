import unittest
from mbpp_404_code import minimum

class TestMinimum(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(minimum(1, 2), 1)
        self.assertEqual(minimum(3, 2), 2)
        self.assertEqual(minimum(5, 5), 5)

    def test_edge_cases(self):
        self.assertEqual(minimum(0, 1), 0)
        self.assertEqual(minimum(-1, 0), -1)
        self.assertEqual(minimum(0, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            minimum('a', 2)
        with self.assertRaises(TypeError):
            minimum(2, 'b')

    def test_boundary_conditions(self):
        self.assertEqual(minimum(1, float('inf')), 1)
        self.assertEqual(minimum(float('-inf'), 2), 2)
