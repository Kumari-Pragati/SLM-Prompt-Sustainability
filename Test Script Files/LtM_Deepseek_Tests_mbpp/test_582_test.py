import unittest
from mbpp_582_code import my_dict

class TestMyDict(unittest.TestCase):
    def test_empty_dict(self):
        self.assertTrue(my_dict({}))

    def test_non_empty_dict(self):
        self.assertFalse(my_dict({"key": "value"}))
