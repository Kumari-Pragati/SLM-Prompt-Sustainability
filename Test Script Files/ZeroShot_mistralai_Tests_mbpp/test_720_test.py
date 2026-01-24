import unittest
from mbpp_720_code import add_dict_to_tuple

class TestAddDictToTuple(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertIsInstance(add_dict_to_tuple((), {}), tuple)
        self.assertEqual(add_dict_to_tuple((), {}), ({},))

    def test_single_tuple_element(self):
        self.assertIsInstance(add_dict_to_tuple((1,), {}), tuple)
        self.assertEqual(add_dict_to_tuple((1,), {}), ((1,), {}))

    def test_multiple_tuple_elements(self):
        self.assertIsInstance(add_dict_to_tuple((1, 2, 3), {}), tuple)
        self.assertEqual(add_dict_to_tuple((1, 2, 3), {}), ((1, 2, 3), {}))

    def test_dict_with_values(self):
        test_dict = {'a': 1, 'b': 2}
        self.assertIsInstance(add_dict_to_tuple((1, 2, 3), test_dict), tuple)
        self.assertEqual(add_dict_to_tuple((1, 2, 3), test_dict), ((1, 2, 3), {'a': 1, 'b': 2}))
