import unittest
from mbpp_648_code import zip_longest, chain, tee
from copy import deepcopy

def exchange_elements(lst):
    lst1, lst2 = tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))

class TestExchangeElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(exchange_elements([]), [])

    def test_single_element(self):
        self.assertEqual(exchange_elements([1]), [1])

    def test_even_length_list(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4]), [2, 1, 4, 3])

    def test_odd_length_list(self):
        self.assertEqual(exchange_elements([1, 2, 3]), [2, 1, 3])

    def test_list_with_duplicates(self):
        self.assertEqual(exchange_elements([1, 1, 2, 2, 3]), [1, 2, 3, 1, 2])

    def test_list_with_non_iterable_element(self):
        with self.assertRaises(TypeError):
            exchange_elements([1, "a", 2])

    def test_list_with_empty_element(self):
        self.assertEqual(exchange_elements([1, None, 2]), [None, 1, 2])

    def test_list_with_list_element(self):
        self.assertEqual(exchange_elements([[1], [2], [3]]), [[2], [1], [3]])

    def test_list_with_tuple_element(self):
        self.assertEqual(exchange_elements([(1,), (2,), (3,)]), [(2,), (1,), (3,)])

    def test_list_with_set_element(self):
        self.assertEqual(exchange_elements([{1}, {2}, {3}]), [{2}, {1}, {3}])
