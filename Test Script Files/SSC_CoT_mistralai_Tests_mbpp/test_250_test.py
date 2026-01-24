import unittest
from mbpp_250_code import count_X

class TestCountX(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_X((1, 2, 'x', 'X', 3), 'x'), 3)
        self.assertEqual(count_X((1, 2, 'X', 'x', 3), 'X'), 2)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_X((), 'x'), 0)
        self.assertEqual(count_X((None,), 'x'), 0)
        self.assertEqual(count_X((1, 2, 'x', 'X', 3, 'x'), 'x'), 4)
        self.assertEqual(count_X((1, 2, 'x', 'X', 3, 'x'), 'X'), 2)

    def test_mixed_types(self):
        self.assertEqual(count_X((1, 2, 'x', 3, 'X'), 'x'), 2)
        self.assertEqual(count_X((1, 2, 3.0, 'X'), 'x'), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_X('string', 'x')
        with self.assertRaises(TypeError):
            count_X((1, 2, 'x'), 3)
