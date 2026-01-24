import unittest
from mbpp_831_code import count_Pairs

class TestCountPairs(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5], 5), 0)

    def test_edge_case(self):
        self.assertEqual(count_Pairs([1, 2, 2, 3, 4], 5), 1)

    def test_edge_case2(self):
        self.assertEqual(count_Pairs([1, 1, 1, 2, 2], 5), 2)

    def test_edge_case3(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5, 5], 6), 1)

    def test_edge_case4(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5, 6], 6), 0)

    def test_edge_case5(self):
        self.assertEqual(count_Pairs([1, 1, 1, 1, 1, 1], 6), 5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Pairs([1, 2, 3], 'a')
