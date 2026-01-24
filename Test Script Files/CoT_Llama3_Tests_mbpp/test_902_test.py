import unittest
from mbpp_902_code import add_dict

class TestAddDict(unittest.TestCase):
    def test_add_dict(self):
        self.assertEqual(add_dict({'a': 1, 'b': 2}, {'b': 3, 'c': 4}), Counter({'a': 1, 'b': 5, 'c': 4}))
        self.assertEqual(add_dict({'a': 1, 'b': 2}, {}), Counter({'a': 1, 'b': 2}))
        self.assertEqual(add_dict({}, {'a': 1, 'b': 2}), Counter({'a': 1, 'b': 2}))
        self.assertEqual(add_dict({'a': 1, 'b': 2}, {'a': 1, 'b': 2}), Counter({'a': 2, 'b': 4}))
        self.assertEqual(add_dict({'a': 1, 'b': 2}, {'a': 3, 'b': 4}), Counter({'a': 4, 'b': 6}))

    def test_add_dict_edge_cases(self):
        self.assertEqual(add_dict({'a': 1, 'b': 2}, {'a': 0, 'b': 0}), Counter({'a': 1, 'b': 2}))
        self.assertEqual(add_dict({'a': 0, 'b': 0}, {'a': 1, 'b': 2}), Counter({'a': 1, 'b': 2}))

    def test_add_dict_invalid_inputs(self):
        with self.assertRaises(TypeError):
            add_dict(None, {'a': 1, 'b': 2})
        with self.assertRaises(TypeError):
            add_dict({'a': 1, 'b': 2}, None)
        with self.assertRaises(TypeError):
            add_dict(None, None)
