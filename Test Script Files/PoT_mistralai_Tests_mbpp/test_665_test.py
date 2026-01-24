import unittest
from mbpp_665_code import move_last

class TestMoveLast(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(move_last([1, 1, 2, 1, 3]), [2, 3])
        self.assertEqual(move_last([1, 1, 1, 2, 1]), [2])
        self.assertEqual(move_last([1, 1, 1, 1, 2]), [2])

    def test_edge_case_single_element(self):
        self.assertEqual(move_last([1]), [])

    def test_edge_case_no_duplicates(self):
        self.assertEqual(move_last([1, 2]), [2, 1])

    def test_edge_case_empty_list(self):
        self.assertEqual(move_last([]), [])

    def test_corner_case_duplicates_at_end(self):
        self.assertEqual(move_last([1, 1, 2, 1]), [2, 1, 1])
