import unittest
from mbpp_967_code import check

class TestCheckFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check("beautiful"), 'accepted')

    def test_boundary_case(self):
        self.assertEqual(check("aeiou"), 'accepted')

    def test_edge_case(self):
        self.assertEqual(check("AEIOU"), 'accepted')
        self.assertEqual(check(""), 'not accepted')

    def test_special_case(self):
        self.assertEqual(check("aeiouy"), 'accepted')
        self.assertEqual(check("AEIOUY"), 'accepted')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check(12345)
        with self.assertRaises(TypeError):
            check(["a", "b", "c"])
