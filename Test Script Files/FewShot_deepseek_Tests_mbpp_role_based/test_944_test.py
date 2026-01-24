import unittest
from mbpp_944_code import num_position

class TestNumPosition(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(num_position("123abc456"), 0)

    def test_edge_condition(self):
        self.assertEqual(num_position(""), None)

    def test_boundary_condition(self):
        self.assertEqual(num_position("abc"), None)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            num_position(123456)
