import unittest
from mbpp_847_code import lcopy

class TestLcopy(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(lcopy([1, 2, 3]), [1, 2, 3])

    def test_empty_input(self):
        self.assertEqual(lcopy([]), [])

    def test_single_element_input(self):
        self.assertEqual(lcopy([4]), [4])

    def test_min_max_values(self):
        self.assertEqual(lcopy(range(-100, 101)), range(-100, 101))

    def test_list_of_lists(self):
        self.assertEqual(lcopy([[1, 2, 3], [4, 5, 6]]), [[1, 2, 3], [4, 5, 6]])

    def test_list_of_tuples(self):
        self.assertEqual(lcopy([(1, 2, 3), (4, 5, 6)]), [(1, 2, 3), (4, 5, 6)])
