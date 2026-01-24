import unittest
from mbpp_63_code import max_difference

class TestMaxDifference(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(max_difference([(1, 2), (3, 4), (5, 6)]), 1)

    def test_edge(self):
        self.assertEqual(max_difference([(1, 1), (2, 2), (3, 3)]), 0)

    def test_edge2(self):
        self.assertEqual(max_difference([(1, 2), (2, 1), (3, 4)]), 1)

    def test_edge3(self):
        self.assertEqual(max_difference([(1, 2), (2, 2), (3, 4)]), 1)

    def test_edge4(self):
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4)]), 1)

    def test_edge5(self):
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5)]), 1)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            max_difference([1, 2, 3])
