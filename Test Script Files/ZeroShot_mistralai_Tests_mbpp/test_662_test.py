import unittest
from mbpp_662_code import MutableMapping
from six.moves import range
from collections import OrderedDict

class TestSortedDict(unittest.TestCase):

    def test_empty_dict(self):
        self.assertIsInstance(sorted_dict({}), MutableMapping)
        self.assertDictEqual(sorted_dict({}), {})

    def test_single_key_dict(self):
        for key, value in [('a', [1, 2, 3]), ('b', [4, 5, 6])]:
            self.assertIsInstance(sorted_dict({key: value}), MutableMapping)
            self.assertDictEqual(sorted_dict({key: value}), {key: sorted(value)})

    def test_multiple_keys_dict(self):
        for keys_values in [
            (('a', [1, 2, 3]), ('b', [4, 5, 6])),
            (('b', [4, 5, 6]), ('a', [1, 2, 3])),
            (('a', [3, 2, 1]), ('b', [6, 5, 4])),
            (('b', [6, 5, 4]), ('a', [3, 2, 1]))
        ]:
            self.assertIsInstance(sorted_dict(OrderedDict(keys_values)), MutableMapping)
            self.assertDictEqual(sorted_dict(OrderedDict(keys_values)), OrderedDict(sorted(keys_values.items())))

    def test_key_value_types(self):
        for key, value in [
            (1, [1, 2, 3]),
            (1.0, [1.0, 2.0, 3.0]),
            (True, [True, False, True]),
            (('a', 'b'), [('a', 'b'), ('c', 'd')])
        ]:
            with self.subTest(key=key, value=value):
                with self.assertRaises(TypeError):
                    sorted_dict({key: value})
