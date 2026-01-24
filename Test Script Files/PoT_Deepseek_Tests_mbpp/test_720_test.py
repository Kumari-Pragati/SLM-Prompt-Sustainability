import unittest
from mbpp_720_code import add_dict_to_tuple

class TestAddDictToTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(add_dict_to_tuple(('a', 'b', 'c'), {'d': 'e'}), (('a', 'b', 'c', {'d': 'e'})))

    def test_empty_tuple(self):
        self.assertEqual(add_dict_to_tuple((), {'d': 'e'}), (({'d': 'e'},)))

    def test_empty_dict(self):
        self.assertEqual(add_dict_to_tuple(('a', 'b', 'c'), {}), (('a', 'b', 'c', {})))

    def test_single_element_tuple(self):
        self.assertEqual(add_dict_to_tuple(('a',), {'d': 'e'}), (('a', {'d': 'e'})))

    def test_large_tuple(self):
        test_dict = {'d': 'e'}
        test_tup = tuple(range(1000))
        expected_tup = test_tup + (test_dict,)
        self.assertEqual(add_dict_to_tuple(test_tup, test_dict), (expected_tup))
