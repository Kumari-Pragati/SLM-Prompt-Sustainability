import unittest
from mbpp_758_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(unique_sublists([[1, 2], [3, 4]]), {(1, 2): 1, (3, 4): 1})

    def test_empty_input(self):
        self.assertEqual(unique_sublists([]), {})

    def test_duplicate_sublists(self):
        self.assertEqual(unique_sublists([[1, 2], [1, 2]]), {(1, 2): 2})

    def test_single_element_sublists(self):
        self.assertEqual(unique_sublists([[1], [2]]), {(1,): 1, (2,): 1})

    def test_same_elements_sublists(self):
        self.assertEqual(unique_sublists([[1, 1], [2, 2]]), {(1, 1): 1, (2, 2): 1})

    def test_large_input(self):
        large_input = [[i for i in range(100)] for _ in range(100)]
        self.assertEqual(unique_sublists(large_input), {tuple(range(100)): 100})
