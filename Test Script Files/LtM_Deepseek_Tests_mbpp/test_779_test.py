import unittest
from mbpp_779_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(unique_sublists([[1, 2, 3], [1, 2, 3]]), {(1, 2, 3): 2})

    def test_edge_condition_empty_input(self):
        self.assertEqual(unique_sublists([]), {})

    def test_boundary_condition_single_sublist(self):
        self.assertEqual(unique_sublists([[1, 2, 3]]), {(1, 2, 3): 1})

    def test_complex_input(self):
        self.assertEqual(unique_sublists([[1, 2, 3], [3, 2, 1], [1, 2, 3]]), {(1, 2, 3): 2, (3, 2, 1): 1})

    def test_duplicate_sublists(self):
        self.assertEqual(unique_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]), {(1, 2, 3): 3})
