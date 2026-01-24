import unittest
from mbpp_322_code import position_min

class TestPositionMin(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(position_min([1, 2, 3, 4, 5]), [0, 1, 2, 3, 4])

    def test_edge_case_min_at_start(self):
        self.assertEqual(position_min([5, 4, 3, 2, 1]), [0, 1, 2, 3, 4])

    def test_edge_case_min_at_end(self):
        self.assertEqual(position_min([1, 2, 3, 4, 5]), [0, 1, 2, 3, 4])

    def test_edge_case_min_at_middle(self):
        self.assertEqual(position_min([5, 4, 3, 2, 1]), [0, 1, 2, 3, 4])

    def test_multiple_min_values(self):
        self.assertEqual(position_min([1, 2, 2, 3, 4]), [0, 2, 3])

    def test_empty_list(self):
        self.assertEqual(position_min([]), [])

    def test_single_element_list(self):
        self.assertEqual(position_min([5]), [0])

    def test_list_with_duplicates(self):
        self.assertEqual(position_min([1, 2, 2, 3, 3, 4, 4, 5]), [0, 1, 2, 3, 4, 5])
