import unittest
from mbpp_627_code import find_First_Missing

class TestFindFirstMissing(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 9), 10)
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 5, 6, 7, 8, 9], 0, 8), 4)

    def test_edge_cases(self):
        self.assertEqual(find_First_Missing([1], 0, 0), 2)
        self.assertEqual(find_First_Missing([0], 0, 0), 1)
        self.assertEqual(find_First_Missing([], 0, -1), 1)

    def test_corner_cases(self):
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 10), 11)
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11], 0, 10), 10)
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12], 0, 10), 11)
