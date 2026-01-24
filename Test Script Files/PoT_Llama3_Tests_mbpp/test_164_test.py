import unittest
from mbpp_164_code import areEquivalent

class TestAreEquivalent(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(areEquivalent(12, 18))

    def test_edge_case1(self):
        self.assertFalse(areEquivalent(12, 15))

    def test_edge_case2(self):
        self.assertTrue(areEquivalent(24, 24))

    def test_edge_case3(self):
        self.assertFalse(areEquivalent(12, 13))

    def test_edge_case4(self):
        self.assertTrue(areEquivalent(36, 36))

    def test_invalid_input1(self):
        with self.assertRaises(TypeError):
            areEquivalent('a', 12)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            areEquivalent(12, 'b')

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            areEquivalent('a', 'b')
