import unittest
from mbpp_925_code import mutiple_tuple

class TestMutipleTuple(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(mutiple_tuple((1,)), 1)

    def test_multiple_elements(self):
        self.assertEqual(mutiple_tuple((1, 2, 3)), 6)

    def test_zero_elements(self):
        self.assertEqual(mutiple_tuple(()), 1)

    def test_negative_elements(self):
        self.assertEqual(mutiple_tuple((-1, 2, 3)), -6)

    def test_mixed_elements(self):
        self.assertEqual(mutiple_tuple((1, -2, 3)), 3)

    def test_non_integer_elements(self):
        self.assertEqual(mutiple_tuple((1, 2.5, 3)), 7.5)

    def test_empty_list(self):
        with self.assertRaises(TypeError):
            mutiple_tuple([])
