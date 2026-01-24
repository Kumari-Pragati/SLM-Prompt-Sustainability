import unittest
from mbpp_61_code import count_Substrings

class TestCountSubstrings(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_Substrings('131', 3), 2)

    def test_edge_case(self):
        self.assertEqual(count_Substrings('', 0), 0)

    def test_boundary_case(self):
        self.assertEqual(count_Substrings('1', 1), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Substrings(123, '3')
