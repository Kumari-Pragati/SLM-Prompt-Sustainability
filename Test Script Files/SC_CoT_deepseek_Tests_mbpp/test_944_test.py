import unittest
from mbpp_944_code import num_position

class TestNumPosition(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(num_position("123abc"), 0)

    def test_edge_case(self):
        self.assertEqual(num_position(""), None)
        self.assertEqual(num_position("abc"), None)

    def test_corner_case(self):
        self.assertEqual(num_position("123abc123"), 0)
        self.assertEqual(num_position("123123"), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            num_position(12345)
