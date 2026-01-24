import unittest
from mbpp_464_code import check_value

class TestCheckValue(unittest.TestCase):

    def test_empty_dict(self):
        with self.assertRaises(KeyError):
            check_value({}, 42)

    def test_single_value_dict(self):
        self.assertTrue(check_value({'key': 42}, 42))

    def test_multiple_values_dict(self):
        self.assertTrue(check_value({'key1': 42, 'key2': 42}, 42))
        self.assertFalse(check_value({'key1': 42, 'key2': 43}, 42))

    def test_mixed_values_dict(self):
        self.assertFalse(check_value({'key1': 42, 'key2': '42'}, 42))
