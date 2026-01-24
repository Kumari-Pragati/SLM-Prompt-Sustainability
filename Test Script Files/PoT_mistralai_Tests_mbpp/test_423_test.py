import unittest
from mbpp_423_code import get_maxgold

class TestGetMaxGold(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_maxgold([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3), 12)
        self.assertEqual(get_maxgold([[1], [2], [3]], 3, 1), 3)
        self.assertEqual(get_maxgold([[1, 2, 3], [4, 5, 6]], 2, 3), 7)

    def test_edge_case(self):
        self.assertEqual(get_maxgold([[1], [2]], 2, 1), 2)
        self.assertEqual(get_maxgold([[1, 2, 3]], 1, 3), 3)
        self.assertEqual(get_maxgold([[1, 2, 3]], 2, 1), 2)

    def test_corner_case(self):
        self.assertEqual(get_maxgold([[1], []], 1, 1), 1)
        self.assertEqual(get_maxgold([[], [1]], 1, 1), 1)
        self.assertEqual(get_maxgold([[1, 2], [3, 4]], 2, 2), 5)
