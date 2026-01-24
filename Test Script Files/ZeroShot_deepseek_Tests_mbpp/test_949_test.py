import unittest
from mbpp_949_code import sort_list

class TestSortList(unittest.TestCase):

    def test_sort_list(self):
        self.assertEqual(sort_list([1, 2, 3, 4, 5]), '[1, 2, 3, 4, 5]')
        self.assertEqual(sort_list([10, 20, 30, 40, 50]), '[10, 20, 30, 40, 50]')
        self.assertEqual(sort_list([100, 200, 300, 400, 500]), '[100, 200, 300, 400, 500]')
        self.assertEqual(sort_list([1, 20, 300, 4000, 50000]), '[1, 20, 300, 4000, 50000]')
        self.assertEqual(sort_list([10, 2, 30, 4, 500]), '[2, 4, 10, 30, 500]')
