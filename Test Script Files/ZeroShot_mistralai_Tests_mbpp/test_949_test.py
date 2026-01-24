import unittest
from mbpp_949_code import sort_list, count_digs

class TestSortList(unittest.TestCase):

    def test_sort_list(self):
        self.assertEqual(sort_list([1, 10, 2, 20, 3, 30]), "[1, 2, 3, 10, 20, 30]")
        self.assertEqual(sort_list([5, 50, 1, 10, 2, 20]), "[1, 2, 5, 10, 50, 20]")
        self.assertEqual(sort_list([100, 10, 1, 200]), "[1, 10, 100, 200]")
        self.assertEqual(sort_list([1, 10, 'a', 'b']), "[1, 10, 'a', 'b']")
        self.assertEqual(sort_list([10, 'a', 20, 'b']), "[10, 'a', 20, 'b']")

    def test_count_digs(self):
        self.assertEqual(count_digs((1, 10, 2, 20)), 3 + 2 + 1 + 2)
        self.assertEqual(count_digs((5, 50, 1, 10, 2, 20)), 1 + 2 + 1 + 2 + 1 + 2 + 2)
        self.assertEqual(count_digs((100, 10, 1, 200)), 3 + 2 + 1 + 3)
        self.assertEqual(count_digs((1, 10, 'a', 'b')), 1 + 2)
        self.assertEqual(count_digs((10, 'a', 20, 'b')), 2 + 1 + 3 + 2)
