import unittest
from mbpp_758_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(unique_sublists([[1, 2], [2, 3], [1, 2]]), {'(1, 2)': 2, '(2, 3)': 3})
        self.assertEqual(unique_sublists([[3, 4], [3, 4, 5], [3, 4]]), {'(3, 4)': 3, '(3, 4, 5)': 5})

    def test_edge_and_boundary_cases(self):
        self.assertEqual(unique_sublists([]), {})
        self.assertEqual(unique_sublists([[1]]), {'(1,)': 1})
        self.assertEqual(unique_sublists([[1, 1]]), {'(1, 1)': 2})
        self.assertEqual(unique_sublists([[1, 2], [1, 2], [1, 2]]), {'(1, 2)': 3})
        self.assertEqual(unique_sublists([[1, 2], [2, 1]]), {'(1, 2)': 2})

    def test_special_cases(self):
        self.assertEqual(unique_sublists([[1, 2, 3], [1, 2], [3, 1]]), {'(1, 2, 3)': 3, '(1, 2)': 2, '(3, 1)': 1})
        self.assertEqual(unique_sublists([[1, 1, 1], [2, 2, 2], [3, 3, 3]]), {'(1, 1, 1)': 3, '(2, 2, 2)': 3, '(3, 3, 3)': 3})
