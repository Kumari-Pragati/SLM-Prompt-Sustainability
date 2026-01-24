import unittest
from mbpp_564_code import count_Pairs

class TestCountPairs(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5], 5), 4)

    def test_edge(self):
        self.assertEqual(count_Pairs([1, 1, 1, 1, 1], 5), 0)

    def test_edge2(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5], 2), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Pairs(None, 5)

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            count_Pairs([], 5)

    def test_single_element_input(self):
        with self.assertRaises(TypeError):
            count_Pairs([1], 5)
