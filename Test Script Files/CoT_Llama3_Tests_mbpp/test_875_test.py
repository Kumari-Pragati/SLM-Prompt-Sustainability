import unittest
from mbpp_875_code import min_difference

class TestMinDifference(unittest.TestCase):

    def test_min_difference_typical(self):
        self.assertEqual(min_difference([(1, 3), (2, 4), (5, 7)]), 1)

    def test_min_difference_edge(self):
        self.assertEqual(min_difference([(1, 1), (2, 2)]), 0)

    def test_min_difference_edge2(self):
        self.assertEqual(min_difference([(1, 2), (2, 1)]), 1)

    def test_min_difference_edge3(self):
        self.assertEqual(min_difference([(1, 1), (1, 1)]), 0)

    def test_min_difference_invalid_input(self):
        with self.assertRaises(TypeError):
            min_difference("test")

    def test_min_difference_empty_input(self):
        with self.assertRaises(IndexError):
            min_difference([])

    def test_min_difference_single_element(self):
        self.assertEqual(min_difference([(1, 1)]), 0)

    def test_min_difference_single_element2(self):
        self.assertEqual(min_difference([(1, 1), (1, 1)]), 0)
