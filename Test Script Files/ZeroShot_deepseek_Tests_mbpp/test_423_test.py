import unittest
from mbpp_423_code import get_maxgold

class TestGetMaxGold(unittest.TestCase):

    def test_get_maxgold(self):
        # Test case 1
        gold = [[1, 3, 3], [2, 1, 4], [0, 6, 4]]
        m = 3
        n = 3
        self.assertEqual(get_maxgold(gold, m, n), 12)

        # Test case 2
        gold = [[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]]
        m = 4
        n = 4
        self.assertEqual(get_maxgold(gold, m, n), 16)

        # Test case 3
        gold = [[1]]
        m = 1
        n = 1
        self.assertEqual(get_maxgold(gold, m, n), 1)

        # Test case 4
        gold = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        m = 3
        n = 3
        self.assertEqual(get_maxgold(gold, m, n), 0)

        # Test case 5
        gold = [[100, 33, 131], [60, 122, 44], [15, 106, 54]]
        m = 3
        n = 3
        self.assertEqual(get_maxgold(gold, m, n), 342)
