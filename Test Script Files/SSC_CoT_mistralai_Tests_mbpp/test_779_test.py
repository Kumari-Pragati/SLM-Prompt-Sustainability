import unittest
from mbpp_779_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(unique_sublists([[1, 2], [2, 3], [1, 2]]), {'((1, 2),)': 2, '((2, 3),)': 3})
        self.assertEqual(unique_sublists([[1], [2], [3]]) , {'((1,),)': 1, '((2,),)': 1, '((3,),)': 1})

    def test_edge_and_boundary_cases(self):
        self.assertEqual(unique_sublists([]), {})
        self.assertEqual(unique_sublists([[1]]), {'((1,),)': 1})
        self.assertEqual(unique_sublists([[1, 1], [2, 2], [3, 3]]), {'((1, 1),)': 2, '((2, 2),)': 2, '((3, 3),)': 2})
        self.assertEqual(unique_sublists([[1, 2], [2, 1]]), {'((1, 2),)': 1, '((2, 1),)': 1})

    def test_special_cases(self):
        self.assertEqual(unique_sublists([[1, 2], [2, 1], [1, 2]]), {'((1, 2),)': 2})
        self.assertEqual(unique_sublists([[1], [1], [1]]), {'((1,),)': 3})
