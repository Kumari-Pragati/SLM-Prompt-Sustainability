import unittest
from mbpp_703_code import Mock

from703_code import is_key_present

class TestIsKeyPresent(unittest.TestCase):

    def test_normal_input(self):
        data = {'key': 'value'}
        self.assertTrue(is_key_present(data, 'key'))

    def test_edge_input(self):
        data = {'key': 'value'}
        self.assertFalse(is_key_present(data, 'another_key'))
        self.assertFalse(is_key_present(data, 123))
        self.assertFalse(is_key_present(data, []))
        self.assertFalse(is_key_present(data, None))

    def test_empty_input(self):
        data = {}
        self.assertFalse(is_key_present(data, 'key'))

    def test_invalid_input(self):
        data = Mock()
        with self.assertRaises(TypeError):
            is_key_present(data, 'key')
