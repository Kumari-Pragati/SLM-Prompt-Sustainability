import unittest
from mbpp_288_code import modular_inverse

class TestModularInverse(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(modular_inverse([1, 2, 3], 3, 5), 1)

    def test_edge_case(self):
        self.assertEqual(modular_inverse([1, 4, 9], 3, 10), 0)

    def test_boundary_case(self):
        self.assertEqual(modular_inverse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 11), 10)

    def test_invalid_input_case(self):
        with self.assertRaises(TypeError):
            modular_inverse("1, 2, 3", 3, 5)
