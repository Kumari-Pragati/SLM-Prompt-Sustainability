import unittest
from mbpp_445_code import index_multiplication

class TestIndexMultiplication(unittest.TestCase):

    def test_index_multiplication(self):
        self.assertEqual(index_multiplication((1, 2, 3), (4, 5, 6)), ((4, 10, 18),))
        self.assertEqual(index_multiplication((-1, 2, -3), (4, -5, 6)), ((-4, -10, -18),))
        self.assertEqual(index_multiplication((1, 0, 3), (0, 5, 0)), ((0, 0, 0),))
        self.assertEqual(index_multiplication((1, 2, 3), (4, 5, 6, 7)), ((4, 10, 18),))
        self.assertEqual(index_multiplication((1, 2, 3, 4), (4, 5, 6)), ((4, 10, 18),))
