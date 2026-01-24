import unittest
from mbpp_445_code import index_multiplication

class TestIndexMultiplication(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(index_multiplication((1, 2, 3), (4, 5, 6)), ((4, 10, 18),))

    def test_edge_cases(self):
        self.assertEqual(index_multiplication((1, 2), (3, 4)), ((3, 8),))
        self.assertEqual(index_multiplication((1), (2)), ((2,)))
        self.assertEqual(index_multiplication((), (1, 2)), ())
        self.assertEqual(index_multiplication((1, 2, 3), ()), ())

    def test_boundary_cases(self):
        self.assertEqual(index_multiplication((1, 2, 3, 4, 5), (1, 2, 3, 4, 5)), ((1, 4, 9, 16, 25),))
        self.assertEqual(index_multiplication((1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5, 6)), ((1, 4, 9, 16, 25, 36),))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            index_multiplication('a', (1, 2, 3))
        with self.assertRaises(TypeError):
            index_multiplication((1, 2, 3), 'a')
