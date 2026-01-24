import unittest
from mbpp_925_code import mutiple_tuple

class TestMutipleTuple(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(mutiple_tuple([1, 2, 3]), 6)
        self.assertEqual(mutiple_tuple([0, 0, 0]), 0)
        self.assertEqual(mutiple_tuple([-1, -2, -3]), 6)

    def test_edge_cases(self):
        self.assertEqual(mutiple_tuple([0]), 0)
        self.assertEqual(mutiple_tuple([1]), 1)
        self.assertEqual(mutiple_tuple([1, ]), 1)
        self.assertEqual(mutiple_tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), 2432902008176640000)

    def test_invalid_input(self):
        self.assertRaises(TypeError, mutiple_tuple, [1, 'a', 3])
        self.assertRaises(TypeError, mutiple_tuple, ['1', 2, 3])
        self.assertRaises(TypeError, mutiple_tuple, [1, 2, 'a'])
