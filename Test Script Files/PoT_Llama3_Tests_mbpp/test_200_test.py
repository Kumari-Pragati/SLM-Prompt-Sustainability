import unittest
from mbpp_200_code import position_max

class TestPositionMax(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(position_max([1, 2, 3, 4, 5]), [4])

    def test_edge_case_max_at_start(self):
        self.assertEqual(position_max([5, 2, 3, 4, 1]), [0])

    def test_edge_case_max_at_end(self):
        self.assertEqual(position_max([1, 2, 3, 4, 5]), [4])

    def test_edge_case_max_at_middle(self):
        self.assertEqual(position_max([1, 2, 5, 4, 3]), [2])

    def test_multiple_max_values(self):
        self.assertEqual(position_max([1, 2, 2, 3, 4]), [1, 2])

    def test_empty_list(self):
        self.assertEqual(position_max([]), [])

    def test_single_element_list(self):
        self.assertEqual(position_max([5]), [0])

    def test_list_with_duplicates(self):
        self.assertEqual(position_max([1, 2, 2, 3, 3, 4]), [1, 2, 3])
