import unittest
from mbpp_711_code import product_Equal

class TestProductEqual(unittest.TestCase):

    def test_product_Equal_typical(self):
        self.assertTrue(product_Equal(123456789))

    def test_product_Equal_edge_case1(self):
        self.assertFalse(product_Equal(9))

    def test_product_Equal_edge_case2(self):
        self.assertTrue(product_Equal(111111111))

    def test_product_Equal_invalid_input1(self):
        with self.assertRaises(TypeError):
            product_Equal('abc')

    def test_product_Equal_invalid_input2(self):
        with self.assertRaises(TypeError):
            product_Equal(None)

    def test_product_Equal_invalid_input3(self):
        with self.assertRaises(TypeError):
            product_Equal([1, 2, 3])

    def test_product_Equal_invalid_input4(self):
        with self.assertRaises(TypeError):
            product_Equal({'a': 1, 'b': 2})

    def test_product_Equal_invalid_input5(self):
        with self.assertRaises(TypeError):
            product_Equal(True)

    def test_product_Equal_invalid_input6(self):
        with self.assertRaises(TypeError):
            product_Equal(False)
