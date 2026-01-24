import unittest

from mbpp_352_code import unique_Characters

class TestUniqueCharacters(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertTrue(unique_Characters("abcde"))

    def test_edge_case(self):
        self.assertTrue(unique_Characters(""))

    def test_corner_case(self):
        self.assertFalse(unique_Characters("aabb"))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            unique_Characters(1234)
