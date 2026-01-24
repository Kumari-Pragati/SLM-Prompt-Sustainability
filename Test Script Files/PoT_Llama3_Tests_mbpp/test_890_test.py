import unittest
from mbpp_890_code import find_Extra

class TestFindExtra(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 6], 5), 4)

    def test_edge_case_equal(self):
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5), 5)

    def test_edge_case_empty(self):
        self.assertEqual(find_Extra([], [], 0), 0)

    def test_edge_case_single(self):
        self.assertEqual(find_Extra([1], [1], 1), 0)

    def test_edge_case_single_diff(self):
        self.assertEqual(find_Extra([1], [2], 1), 0)

    def test_edge_case_single_same(self):
        self.assertEqual(find_Extra([1], [1], 1), 0)

    def test_edge_case_single_diff(self):
        self.assertEqual(find_Extra([1], [2], 1), 0)

    def test_edge_case_single_same(self):
        self.assertEqual(find_Extra([1], [1], 1), 0)

    def test_edge_case_single_diff(self):
        self.assertEqual(find_Extra([1], [2], 1), 0)

    def test_edge_case_single_same(self):
        self.assertEqual(find_Extra([1], [1], 1), 0)

    def test_edge_case_single_diff(self):
        self.assertEqual(find_Extra([1], [2], 1), 0)

    def test_edge_case_single_same(self):
        self.assertEqual(find_Extra([1], [1], 1), 0)

    def test_edge_case_single_diff(self):
        self.assertEqual(find_Extra([1], [2], 1), 0)

    def test_edge_case_single_same(self):
        self.assertEqual(find_Extra([1], [1], 1), 0)
