import unittest
from mbpp_578_code import interleave_lists

class TestInterleaveLists(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(interleave_lists([1, 2, 3], [4, 5, 6], [7, 8, 9]), [1, 4, 7, 2, 5, 8, 3, 6, 9])

    def test_edge_case_empty_list1(self):
        self.assertEqual(interleave_lists([], [1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_edge_case_empty_list2(self):
        self.assertEqual(interleave_lists([1, 2, 3], [], [4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_edge_case_empty_list3(self):
        self.assertEqual(interleave_lists([], [], [1, 2, 3]), [1, 2, 3])

    def test_edge_case_single_list(self):
        self.assertEqual(interleave_lists([1, 2, 3], [], []), [1, 2, 3])

    def test_edge_case_single_list2(self):
        self.assertEqual(interleave_lists([], [1, 2, 3], []), [1, 2, 3])

    def test_edge_case_single_list3(self):
        self.assertEqual(interleave_lists([], [], [1, 2, 3]), [1, 2, 3])

    def test_edge_case_all_empty(self):
        self.assertEqual(interleave_lists([], [], []), [])
