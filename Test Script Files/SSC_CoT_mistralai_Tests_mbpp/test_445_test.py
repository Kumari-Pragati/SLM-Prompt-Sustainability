import unittest
from mbpp_445_code import index_multiplication

class TestIndexMultiplication(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(index_multiplication((1, 2, 3), (4, 5, 6)), ((1 * 4, 2 * 5, 3 * 6), (4 * 1, 5 * 2, 6 * 3)))
        self.assertEqual(index_multiplication((0, 0, 0), (1, 2, 3)), ((0 * 1, 0 * 2, 0 * 3), (1 * 0, 2 * 0, 3 * 0)))

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(index_multiplication((1,), (1,)), ((1 * 1,),))
        self.assertEqual(index_multiplication((1, 2), (3,)), ((1 * 3, 2 * 3),))
        self.assertEqual(index_multiplication((1, 2, 3), (4,)), ((1 * 4, 2 * 4, 3 * 4),))
        self.assertEqual(index_multiplication((1, 2, 3), (4, 5)), ((1 * 4, 2 * 5, 3 * 5), (1 * 4, 2 * 5, 3 * 5)))
        self.assertEqual(index_multiplication((1, 2, 3), (4, 5, 6)), ((1 * 4, 2 * 5, 3 * 6), (1 * 4, 2 * 5, 3 * 6), (1 * 4, 2 * 5, 3 * 6)))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            index_multiplication('a', 'b')
        with self.assertRaises(TypeError):
            index_multiplication([1, 2], 'a')
        with self.assertRaises(TypeError):
            index_multiplication('a', [1, 2])
