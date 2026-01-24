import unittest
from mbpp_779_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):

    def test_typical_case(self):
        self.assertDictEqual(unique_sublists([[1, 2], [1, 2, 3], [1, 2]]), {'((1, 2),)': 3})

    def test_edge_case_empty_list(self):
        self.assertDictEqual(unique_sublists([]), {})

    def test_edge_case_single_element_list(self):
        self.assertDictEqual(unique_sublists([[1]]), {'((1,),)': 1})

    def test_edge_case_duplicate_sublists(self):
        self.assertDictEqual(unique_sublists([[1, 2], [1, 2]]), {'((1, 2),)': 2})

    def test_corner_case_sublists_with_different_lengths(self):
        self.assertDictEqual(unique_sublists([[1, 2], [1], [2]]), {'((1,),)': 1, '((2,),)': 1})

    def test_corner_case_sublists_with_repeated_elements(self):
        self.assertDictEqual(unique_sublists([[1, 1], [2, 2]]), {'((1, 1),)': 2, '((2, 2),)': 2})
