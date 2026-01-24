import unittest
from mbpp_750_code import add_tuple

class TestAddTuple(unittest.TestCase):

    def test_simple_addition(self):
        test_list = [1, 2, 3]
        test_tup = (4, 5)
        self.assertEqual(add_tuple(test_list, test_tup), [1, 2, 3, 4, 5])

    def test_empty_list(self):
        test_list = []
        test_tup = (4, 5)
        self.assertEqual(add_tuple(test_list, test_tup), [4, 5])

    def test_empty_tuple(self):
        test_list = [1, 2, 3]
        test_tup = ()
        self.assertEqual(add_tuple(test_list, test_tup), [1, 2, 3])

    def test_mixed_types(self):
        test_list = [1, 'two', 3]
        test_tup = (4, 'five')
        self.assertEqual(add_tuple(test_list, test_tup), [1, 'two', 3, 4, 'five'])

    def test_large_numbers(self):
        test_list = [1000000, 2000000, 3000000]
        test_tup = (4000000, 5000000)
        self.assertEqual(add_tuple(test_list, test_tup), [1000000, 2000000, 3000000, 4000000, 5000000])
