import unittest
from mbpp_720_code import add_dict_to_tuple

class TestAddDictToTuple(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': 4}
        expected_result = (1, 2, 3, {'a': 4})
        self.assertEqual(add_dict_to_tuple(test_tup, test_dict), expected_result)

    def test_empty_tuple(self):
        test_tup = ()
        test_dict = {'a': 4}
        expected_result = ({'a': 4},)
        self.assertEqual(add_dict_to_tuple(test_tup, test_dict), expected_result)

    def test_empty_dict(self):
        test_tup = (1, 2, 3)
        test_dict = {}
        expected_result = (1, 2, 3)
        self.assertEqual(add_dict_to_tuple(test_tup, test_dict), expected_result)

    def test_error_handling(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': 4, 'b': 5}
        with self.assertRaises(TypeError):
            add_dict_to_tuple(test_tup, test_dict)
