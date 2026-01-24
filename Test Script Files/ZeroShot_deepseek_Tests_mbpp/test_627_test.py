import unittest
from mbpp_627_code import find_First_Missing

class TestFindFirstMissing(unittest.TestCase):

    def test_find_First_Missing(self):
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5, 6, 7, 8], 0, 8), 9)
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 6, 7, 8], 0, 7), 5)
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5, 6, 8], 0, 7), 7)
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5, 6, 7], 0, 7), 8)
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5, 6, 7, 9], 0, 8), 8)
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 10), 11)
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 10], 0, 9), 9)
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 9), 10)
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12], 0, 11), 10)
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12], 0, 11), 11)
