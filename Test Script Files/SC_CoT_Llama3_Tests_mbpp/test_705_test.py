import unittest
from mbpp_705_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_sort_sublists_typical(self):
        self.assertEqual(sort_sublists([3, 1, 2]), [[1, 2, 3]])

    def test_sort_sublists_edge_case(self):
        self.assertEqual(sort_sublists(['apple', 'banana', 'cherry']), ['cherry', 'banana', 'apple'])

    def test_sort_sublists_edge_case2(self):
        self.assertEqual(sort_sublists(['a', 'b', 'c']), ['c', 'b', 'a'])

    def test_sort_sublists_edge_case3(self):
        self.assertEqual(sort_sublists([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_sort_sublists_edge_case4(self):
        self.assertEqual(sort_sublists(['a', 'b', 'c', 'd']), ['d', 'c', 'b', 'a'])

    def test_sort_sublists_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_sort_sublists_single_element(self):
        self.assertEqual(sort_sublists([1]), [[1]])

    def test_sort_sublists_single_element2(self):
        self.assertEqual(sort_sublists(['a']), [['a']])

    def test_sort_sublists_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_sublists("Invalid input")
