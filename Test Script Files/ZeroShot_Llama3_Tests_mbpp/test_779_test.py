import unittest
from mbpp_779_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(unique_sublists([]), {})

    def test_single_element_list(self):
        self.assertEqual(unique_sublists([[1]]), {(1,): 1})

    def test_multiple_elements_list(self):
        self.assertEqual(unique_sublists([[1, 2], [1, 2], [3, 4]]), {(1, 2): 2, (3, 4): 1})

    def test_duplicates(self):
        self.assertEqual(unique_sublists([[1, 2], [1, 2], [1, 2]]), {(1, 2): 3})

    def test_empty_sublist(self):
        self.assertEqual(unique_sublists([[1, 2], [], [3, 4]]), {(1, 2): 1, (3, 4): 1})

    def test_sublist_order(self):
        self.assertEqual(unique_sublists([[1, 2], [2, 1], [3, 4]]), {(1, 2): 2, (2, 1): 2, (3, 4): 1})
