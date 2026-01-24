import unittest
from mbpp_684_code import count_Char

class TestCountChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Char("aab", "a"), 2)

    def test_edge_case(self):
        self.assertEqual(count_Char("", "a"), 0)

    def test_boundary_case(self):
        self.assertEqual(count_Char("a"*10000, "a"), 10000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Char(123, "a")
        with self.assertRaises(TypeError):
            count_Char("aab", 123)
