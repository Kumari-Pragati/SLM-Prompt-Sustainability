import unittest
from mbpp_890_code import find_Extra

class TestFindExtra(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Extra([1, 2, 3, 4], [1, 2, 3, 5], 4), 3)
        self.assertEqual(find_Extra([1, 1, 1, 1], [1, 2, 3, 4], 4), 0)
        self.assertEqual(find_Extra([1, 2, 3, 4], [1, 2, 3, 4], 4), 4)

    def test_edge_case_1(self):
        self.assertEqual(find_Extra([1, 2, 3, 4], [], 4), -1)

    def test_edge_case_2(self):
        self.assertEqual(find_Extra([], [1, 2, 3, 4], 4), -1)

    def test_edge_case_3(self):
        self.assertEqual(find_Extra([1, 2, 3, 4], [1, 2, 3, 4, 5], 5), -1)
