import unittest
from mbpp_533_code import remove_datatype

class TestRemoveDatatype(unittest.TestCase):
    def test_remove_string_from_list_of_strings(self):
        self.assertEqual(remove_datatype(('a', 'b', 'c', 1), str), ('a', 'b', 'c'))

    def test_remove_integer_from_list_of_integers(self):
        self.assertEqual(remove_datatype((1, 2, 3, 'a'), int), (1, 2, 3))

    def test_remove_float_from_list_of_floats(self):
        self.assertEqual(remove_datatype((1.0, 2.0, 3.0, 'a'), float), (1.0, 2.0, 3.0))

    def test_remove_list_from_list_of_lists(self):
        self.assertEqual(remove_datatype([('a', 'b'), [1, 2], 'c'], list), [('a', 'b')])

    def test_remove_tuple_from_list_of_tuples(self):
        self.assertEqual(remove_datatype(((1, 'a'), (2, 'b')), tuple), [(1, 'a'), (2, 'b')])

    def test_remove_dict_from_list_of_dicts(self):
        self.assertEqual(remove_datatype([{'a': 1}, {'b': 2}, {'c': 'd'}], dict), [{'a': 1}, {'b': 2}])

    def test_remove_set_from_list_of_sets(self):
        self.assertEqual(remove_datatype({frozenset((1, 'a')), frozenset((2, 'b'))}, set), frozenset((1, 'a')))

    def test_remove_none_from_list_of_nones(self):
        self.assertEqual(remove_datatype([None, None, None], NoneType), [None, None])

    def test_remove_bool_from_list_of_bools(self):
        self.assertEqual(remove_datatype([True, False, True], bool), [True, False])
