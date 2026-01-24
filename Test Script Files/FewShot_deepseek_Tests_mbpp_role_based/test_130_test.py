import unittest
from mbpp_130_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), (3, 3))

    def test_edge_case(self):
        self.assertEqual(max_occurrences([]), None)

    def test_boundary_case(self):
        self.assertEqual(max_occurrences([1]), (1, 1))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_occurrences('1234')
