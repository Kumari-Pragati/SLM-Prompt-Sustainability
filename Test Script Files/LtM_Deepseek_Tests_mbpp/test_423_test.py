import unittest
from mbpp_423_code import get_maxgold

class TestGetMaxGold(unittest.TestCase):

    def test_simple_input(self):
        gold = [[1, 3, 3], [2, 1, 4], [0, 6, 4]]
        self.assertEqual(get_maxgold(gold, 3, 3), 12)

    def test_edge_conditions(self):
        # Test with empty gold array
        self.assertEqual(get_maxgold([[]], 0, 0), 0)
        # Test with single element in gold array
        self.assertEqual(get_maxgold([[5]], 1, 1), 5)
        # Test with maximum values
        self.assertEqual(get_maxgold([[1000, 1000, 1000]], 1, 3), 3000)

    def test_complex_cases(self):
        # Test with multiple rows and columns
        gold = [[1, 3, 3, 2], [2, 1, 4, 1], [5, 6, 4, 2], [3, 2, 1, 4]]
        self.assertEqual(get_maxgold(gold, 4, 4), 16)
        # Test with no gold in the field
        gold = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(get_maxgold(gold, 3, 3), 0)
