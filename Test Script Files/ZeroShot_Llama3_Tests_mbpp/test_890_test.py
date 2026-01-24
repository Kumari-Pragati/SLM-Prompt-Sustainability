import unittest
from mbpp_890_code import find_Extra

class TestFindExtra(unittest.TestCase):

    def test_find_extra(self):
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 6], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 7], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 5, 6], 5), 3)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 4), 4)

    def test_find_extra_edge_cases(self):
        self.assertEqual(find_Extra([], [], 0), 0)
        self.assertEqual(find_Extra([1], [1], 1), 1)
        self.assertEqual(find_Extra([1, 2], [1, 2], 2), 2)
