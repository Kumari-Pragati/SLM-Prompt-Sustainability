import unittest
from mbpp_696_code import map
from six.moves import range
from six.moves import zip

from696_code import zip_list

class TestZipList(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(zip_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertEqual(zip_list([], []), [])
        self.assertEqual(zip_list([1], []), [])
        self.assertEqual(zip_list([], [1]), [])

    def test_edge_cases(self):
        self.assertEqual(zip_list([1], [2, 3]), [2, 3])
        self.assertEqual(zip_list([1, 2], [3]), [3, 3])
        self.assertEqual(zip_list([1, 2, 3], [4]), [4, 4, 3])
        self.assertEqual(zip_list([1, 2, 3], [4, 5]), [5, 6, 3])
        self.assertEqual(zip_list([1, 2, 3], [4, 5, 6]), [5, 6, 7])

    def test_complex(self):
        self.assertEqual(zip_list(range(5), range(5, 10)), [5, 6, 7, 8, 9])
        self.assertEqual(zip_list(range(5), range(10, 15)), [10, 11, 12, 13, 14])
        self.assertEqual(zip_list(range(5), range(15, 20)), [15, 16, 17, 18, 19])
        self.assertEqual(zip_list(range(5), range(20, 25)), [20, 21, 22, 23, 24])
