import unittest
from mbpp_460_code import Extract

class TestExtract(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Extract([(1,), (2, 3), (4, 5, 6)]), [1, 2, 4])

    def test_edge_case_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_edge_case_single_item(self):
        self.assertEqual(Extract([(1,)]), [1])

    def test_edge_case_multiple_items_no_tuples(self):
        self.assertEqual(Extract([1, 2, 3]), [1, 2, 3])

    def test_corner_case_empty_tuple(self):
        self.assertEqual(Extract([(), (1,)]), [1])
