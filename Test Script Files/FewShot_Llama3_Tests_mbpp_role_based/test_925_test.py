import unittest
from mbpp_925_code import mutiple_tuple

class TestMultipleTuple(unittest.TestCase):
    def test_single_element_tuple(self):
        self.assertEqual(mutiple_tuple((5,)), 5)

    def test_multiple_elements_tuple(self):
        self.assertEqual(mutiple_tuple((1, 2, 3, 4)), 24)

    def test_zero_element_tuple(self):
        self.assertEqual(mutiple_tuple(()), 1)

    def test_negative_elements_tuple(self):
        self.assertEqual(mutiple_tuple((-1, -2, -3)), -6)

    def test_mixed_elements_tuple(self):
        self.assertEqual(mutiple_tuple((1, 2, -3, 4)), -6)

    def test_non_integer_elements_tuple(self):
        with self.assertRaises(TypeError):
            mutiple_tuple((1, 2, 3.5))
