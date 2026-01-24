import unittest
from mbpp_919_code import multiply_list

class TestMultiplyList(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(multiply_list([1, 2, 3, 4]), 24)

    def test_edge_condition(self):
        self.assertEqual(multiply_list([0]), 0)

    def test_boundary_condition(self):
        self.assertEqual(multiply_list([1]), 1)
        self.assertEqual(multiply_list([-1]), -1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            multiply_list('123')
        with self.assertRaises(TypeError):
            multiply_list(123)
        with self.assertRaises(TypeError):
            multiply_list([1, '2', 3])
