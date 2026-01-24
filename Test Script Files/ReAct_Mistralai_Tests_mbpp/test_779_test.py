import unittest
from mbpp_779_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(unique_sublists([]), {})

    def test_single_element_list(self):
        self.assertEqual(unique_sublists([[1]]), {'((1,))': 1})

    def test_simple_list(self):
        self.assertEqual(unique_sublists([[1, 2], [2, 3], [1, 2, 3]]),
                         {'((1, 2),)': 2, '((1, 2, 3),)': 1})

    def test_duplicate_sublists(self):
        self.assertEqual(unique_sublists([[1, 2], [2, 1], [1, 2]]),
                         {'((1, 2),)': 2})

    def test_mixed_lists(self):
        self.assertEqual(unique_sublists([[1, 2], [2, 3], [1, 2, 3], [3, 2, 1]]),
                         {'((1, 2),)': 2, '((1, 2, 3),)': 1, '((3, 2, 1),)': 1})

    def test_long_list(self):
        long_list = [[1] * i for i in range(1, 11)]
        self.assertEqual(unique_sublists(long_list), {'((1,),)': 10})

    def test_list_with_empty_sublist(self):
        self.assertEqual(unique_sublists([[1], [], [2]]), {'((1,),)': 1, '((2,),)': 1})

    def test_list_with_only_empty_sublists(self):
        self.assertEqual(unique_sublists([[]]), {'(): 0'})
