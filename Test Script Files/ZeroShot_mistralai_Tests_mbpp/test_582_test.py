import unittest
from mbpp_582_code import my_dict

class TestMyDict(unittest.TestCase):

    def test_empty_dict(self):
        self.assertTrue(my_dict({}))

    def test_non_empty_dict(self):
        self.assertFalse(my_dict({"key": "value"}))

    def test_empty_list_as_dict(self):
        self.assertTrue(my_dict({}))

    def test_list_as_dict(self):
        self.assertFalse(my_dict({[1, 2, 3]}))

    def test_empty_set_as_dict(self):
        self.assertTrue(my_dict({set()}})

    def test_set_as_dict(self):
        self.assertFalse(my_dict({set([1, 2, 3])}})

    def test_empty_tuple_as_dict(self):
        self.assertTrue(my_dict({tuple()}})

    def test_tuple_as_dict(self):
        self.assertFalse(my_dict({(1, 2, 3)}}))
