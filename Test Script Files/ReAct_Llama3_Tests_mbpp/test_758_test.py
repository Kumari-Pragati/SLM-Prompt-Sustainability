import unittest
from mbpp_758_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(unique_sublists([]), {})

    def test_single_sublist(self):
        self.assertEqual(unique_sublists([[1, 2, 3]]), {(1, 2, 3): 1})

    def test_multiple_sublists(self):
        self.assertEqual(unique_sublists([[1, 2, 3], [4, 5, 6], [1, 2, 3]]), {(1, 2, 3): 2})

    def test_sublists_with_duplicates(self):
        self.assertEqual(unique_sublists([[1, 2, 3], [1, 2, 3], [4, 5, 6]]), {(1, 2, 3): 2})

    def test_sublists_with_duplicates_and_empty(self):
        self.assertEqual(unique_sublists([[1, 2, 3], [1, 2, 3], [], [4, 5, 6]]), {(1, 2, 3): 2, (): 1})

    def test_sublists_with_duplicates_and_empty_and_duplicates(self):
        self.assertEqual(unique_sublists([[1, 2, 3], [1, 2, 3], [], [1, 2, 3], [4, 5, 6]]), {(1, 2, 3): 3, (): 1})
