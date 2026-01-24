import unittest
from mbpp_627_code import find_First_Missing

class TestFindFirstMissing(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_FirstMissing([1, 2, 3, 4, 6, 7, 8], 0, 8), 5)
        self.assertEqual(find_First_Missing([-1, 0, 1, 3, 4, 6, 7, 8], 0, 8), -2)
        self.assertEqual(find_First_Missing([1, 2, 3, 4, 5, 6, 7, 8], 0, 8), None)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(find_First_Missing([], 0, 0), 1)
        self.assertEqual(find_First_Missing([1], 0, 0), 1)
        self.assertEqual(find_First_Missing([1, 2], 0, 1), None)
        self.assertEqual(find_First_Missing([1, 2], 1, 1), None)
        self.assertEqual(find_First_Missing([1, 2], 0, 2), 1)
        self.assertEqual(find_First_Missing([1, 2], 2, 2), None)
        self.assertEqual(find_First_Missing([1, 2], -1, 2), -1)
        self.assertEqual(find_First_Missing([1, 2], 2, -1), None)
