import unittest
from mbpp_144_code import sum_Pairs

class TestSumPairs(unittest.TestCase):

    def test_typical(self):
        self.assertEqual(sum_Pairs([1, 2, 3, 4, 5], 5), 10)

    def test_edge1(self):
        self.assertEqual(sum_Pairs([1, 2, 3], 3), 3)

    def test_edge2(self):
        self.assertEqual(sum_Pairs([1, 2], 2), 0)

    def test_edge3(self):
        self.assertEqual(sum_Pairs([1], 1), 0)

    def test_edge4(self):
        self.assertEqual(sum_Pairs([], 0), 0)

    def test_invalid_input1(self):
        with self.assertRaises(TypeError):
            sum_Pairs('abc', 5)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            sum_Pairs([1, 2, 3], 'abc')

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            sum_Pairs([1, 2, 3], 0)
