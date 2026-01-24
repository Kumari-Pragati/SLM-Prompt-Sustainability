import unittest
from mbpp_658_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 4, 4, 4]), 4)

    def test_edge_case(self):
        self.assertEqual(max_occurrences([1]), 1)

    def test_edge_case2(self):
        self.assertEqual(max_occurrences([1, 1, 1, 1]), 1)

    def test_edge_case3(self):
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5]), 1)

    def test_edge_case4(self):
        self.assertEqual(max_occurrences([]), None)

    def test_edge_case5(self):
        self.assertEqual(max_occurrences([1, 1, 1, 1, 1]), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_occurrences("Hello")
