import unittest
from mbpp_779_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):

    def test_simple_list(self):
        self.assertDictEqual(unique_sublists([[1], [2], [1, 2]]), {'(1,)': 1, '(2,)': 1, '(1, 2)': 1})

    def test_empty_list(self):
        self.assertDictEqual(unique_sublists([]), {})

    def test_single_element_list(self):
        self.assertDictEqual(unique_sublists([[1]]), {'(1,)': 1})

    def test_duplicate_sublists(self):
        self.assertDictEqual(unique_sublists([[1], [1], [2]]), {'(1,)': 2, '(2,)': 1})

    def test_negative_numbers(self):
        self.assertDictEqual(unique_sublists([[-1], [2], [-1, 2]]), {'(-1,)': 1, '(2,)': 1, '(-1, 2)': 1})

    def test_mixed_numbers(self):
        self.assertDictEqual(unique_sublists([[1, -2], [3], [1, -2, 3]]), {'(1, -2)': 1, '(3,)': 1, '(1, -2, 3)': 1})
