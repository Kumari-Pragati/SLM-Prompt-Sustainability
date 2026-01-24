import unittest
from mbpp_758_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(unique_sublists([[1, 2], [3, 4], [1, 2]]), {(1, 2): 2, (3, 4): 1})

    def test_empty_list(self):
        self.assertEqual(unique_sublists([]), {})

    def test_single_sublist(self):
        self.assertEqual(unique_sublists([[1, 2]]), {(1, 2): 1})

    def test_duplicate_sublists(self):
        self.assertEqual(unique_sublists([[1, 2], [1, 2]]), {(1, 2): 2})

    def test_sublists_with_same_elements(self):
        self.assertEqual(unique_sublists([[1, 2], [2, 1]]), {(1, 2): 2})

    def test_sublists_with_same_order(self):
        self.assertEqual(unique_sublists([[1, 2], [2, 1]]), {(1, 2): 2})

    def test_sublists_with_different_order(self):
        self.assertEqual(unique_sublists([[2, 1], [1, 2]]), {(1, 2): 2})

    def test_large_input(self):
        large_list = [[i, i+1] for i in range(1000)]
        self.assertEqual(unique_sublists(large_list), {(i, i+1): 1 for i in range(1000)})
