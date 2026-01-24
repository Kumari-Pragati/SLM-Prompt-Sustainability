import unittest
from mbpp_611_code import max_of_nth

class TestMaxOfNth(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), 2)
        self.assertEqual(max_of_nth([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]], 2), -5)
        self.assertEqual(max_of_nth([[0, 0, 0], [1, 1, 1], [2, 2, 2]], 0), 0)
        self.assertEqual(max_of_nth([[10, 20, 30], [40, 50, 60], [70, 80, 90]], -1), 100)

    def test_edge_case_empty_list(self):
        self.assertIsNone(max_of_nth([], 0))

    def test_edge_case_empty_sublist(self):
        self.assertIsNone(max_of_nth([[1], [], [3]], 1))

    def test_edge_case_negative_n(self):
        self.assertIsNone(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1))

    def test_edge_case_non_integer_n(self):
        self.assertIsNone(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'a'))
