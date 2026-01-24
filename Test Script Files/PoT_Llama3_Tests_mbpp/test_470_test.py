import unittest
from mbpp_470_code import add_pairwise

class TestAddPairwise(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(add_pairwise((1, 2, 3)), (2, 3, 4))

    def test_edge(self):
        self.assertEqual(add_pairwise((1,)), ())

    def test_edge2(self):
        self.assertEqual(add_pairwise(()), ())

    def test_edge3(self):
        self.assertEqual(add_pairwise((1, 1)), (2,))

    def test_edge4(self):
        self.assertEqual(add_pairwise((1, 2, 1)), (2, 3, 2))

    def test_invalid(self):
        with self.assertRaises(TypeError):
            add_pairwise("test")
