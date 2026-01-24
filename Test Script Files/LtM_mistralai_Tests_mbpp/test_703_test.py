import unittest
from mbpp_703_code import is_key_present

class TestIsKeyPresent(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(is_key_present({1: 1, 2: 2}, 1))
        self.assertFalse(is_key_present({1: 1, 2: 2}, 3))

    def test_edge_cases(self):
        self.assertTrue(is_key_present({}, 0))
        self.assertFalse(is_key_present({1: 1}, 3))
        self.assertTrue(is_key_present({1: 1}, 1))

    def test_complex(self):
        self.assertTrue(is_key_present({None: 1, 1: 1, 'str': 1}, None))
        self.assertFalse(is_key_present({None: 1, 1: 1, 'str': 1}, 'not_a_key'))
