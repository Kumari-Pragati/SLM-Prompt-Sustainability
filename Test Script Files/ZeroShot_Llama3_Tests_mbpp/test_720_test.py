import unittest
from mbpp_720_code import add_dict_to_tuple

class TestAddDictToTuple(unittest.TestCase):

    def test_add_dict_to_tuple(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': 'b', 'c': 'd'}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], 1)
        self.assertEqual(result[1], 2)
        self.assertEqual(result[2], 3)
        self.assertEqual(result[3], test_dict)

    def test_add_dict_to_tuple_empty(self):
        test_tup = ()
        test_dict = {'a': 'b', 'c': 'd'}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], test_dict)

    def test_add_dict_to_tuple_single(self):
        test_tup = (1,)
        test_dict = {'a': 'b', 'c': 'd'}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 1)
        self.assertEqual(result[1], test_dict)
