import unittest
from mbpp_423_code import get_maxgold

class TestGetMaxGold(unittest.TestCase):

    def test_get_maxgold(self):
        gold = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m = 3
        n = 3
        self.assertEqual(get_maxgold(gold, m, n), 10)

        gold = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        m = 3
        n = 4
        self.assertEqual(get_maxgold(gold, m, n), 14)

        gold = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
        m = 3
        n = 5
        self.assertEqual(get_maxgold(gold, m, n), 16)

        gold = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
        m = 3
        n = 6
        self.assertEqual(get_maxgold(gold, m, n), 18)
