import unittest
from mbpp_352_code import unique_Characters

class TestUniqueCharacters(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(unique_Characters('abcdefg'))

    def test_edge_case(self):
        self.assertTrue(unique_Characters(''))

    def test_boundary_case(self):
        self.assertTrue(unique_Characters('a'))
        self.assertFalse(unique_Characters('aa'))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            unique_Characters(12345)
