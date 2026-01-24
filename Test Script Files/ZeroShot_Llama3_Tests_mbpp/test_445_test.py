import unittest
from mbpp_445_code import index_multiplication

class TestIndexMultiplication(unittest.TestCase):

    def test_index_multiplication(self):
        self.assertEqual(index_multiplication((1, 2, 3), (4, 5, 6)), ((4, 10, 18),))
        self.assertEqual(index_multiplication((1, 2, 3, 4), (5, 6, 7, 8)), ((5, 12, 21, 32),))
        self.assertEqual(index_multiplication((1, 2, 3, 4, 5), (6, 7, 8, 9, 10)), ((6, 14, 24, 40, 50),))
        self.assertEqual(index_multiplication((1, 2, 3), ()), ())
        self.assertEqual(index_multiplication((), (1, 2, 3)), ())
        self.assertEqual(index_multiplication((1, 2, 3), (4, 5)), ((4, 10),))
        self.assertEqual(index_multiplication((1, 2), (3, 4, 5)), ((3, 8),))
