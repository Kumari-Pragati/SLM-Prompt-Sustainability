import unittest
from mbpp_288_code import modular_inverse

class TestModularInverse(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(modular_inverse([2, 3, 4, 5], 4, 7), 1)

    def test_edge_case(self):
        self.assertEqual(modular_inverse([1, 2, 3, 4], 4, 7), 1)

    def test_edge_case2(self):
        self.assertEqual(modular_inverse([2, 3, 4, 5], 4, 1), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            modular_inverse("hello", 4, 7)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            modular_inverse([1, 2, 3, 4], "hello", 7)

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            modular_inverse([1, 2, 3, 4], 4, "hello")
