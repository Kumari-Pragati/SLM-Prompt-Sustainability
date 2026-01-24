import unittest
from mbpp_925_code import mutiple_tuple

class TestMultipleTuple(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(mutiple_tuple([1, 2, 3]), 6)
        self.assertEqual(mutiple_tuple([-1, 2, -3]), 12)
        self.assertEqual(mutiple_tuple([0, 0, 0]), 0)

    def test_edge_cases(self):
        self.assertEqual(mutiple_tuple([1]), 1)
        self.assertEqual(mutiple_tuple([1, 0]), 0)
        self.assertEqual(mutiple_tuple([-1, -1]), 1)

    def test_complex(self):
        self.assertEqual(mutiple_tuple([10, 20, 30, 40]), 12072000)
        self.assertEqual(mutiple_tuple([-10, -20, -30, -40]), 12072000)
        self.assertEqual(mutiple_tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3628800)
