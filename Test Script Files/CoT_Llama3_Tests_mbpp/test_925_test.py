import unittest
from mbpp_925_code import mutiple_tuple

class TestMutipleTuple(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(mutiple_tuple((1, 2, 3)), 6)

    def test_edge_case_zero(self):
        self.assertEqual(mutiple_tuple((0,)), 0)

    def test_edge_case_one(self):
        self.assertEqual(mutiple_tuple((1,)), 1)

    def test_edge_case_negative(self):
        self.assertEqual(mutiple_tuple((-1, 2, 3)), -6)

    def test_edge_case_empty(self):
        self.assertEqual(mutiple_tuple(()), 1)

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            mutiple_tuple([1, 2, 3])

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            mutiple_tuple(("a", 2, 3))
