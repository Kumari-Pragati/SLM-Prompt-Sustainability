import unittest
from mbpp_74_code import is_samepatterns

class TestIsSamePatterns(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_samepatterns(['red', 'green', 'blue'], ['1', '2', '3']))

    def test_edge_case(self):
        self.assertFalse(is_samepatterns(['red', 'green'], ['1', '2', '3']))

    def test_corner_case(self):
        self.assertTrue(is_samepatterns(['red', 'red', 'red'], ['1', '1', '1']))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_samepatterns(['red', 'green'], ['1', '2', 3])
