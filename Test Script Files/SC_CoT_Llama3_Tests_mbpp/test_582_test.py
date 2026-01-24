import unittest
from mbpp_582_code import my_dict

class TestMyDict(unittest.TestCase):

    def test_true(self):
        self.assertTrue(my_dict({}))

    def test_false(self):
        self.assertFalse(my_dict({"a":1}))

    def test_empty_string(self):
        self.assertTrue(my_dict({}))

    def test_non_dict_input(self):
        with self.assertRaises(TypeError):
            my_dict("")

    def test_non_dict_input2(self):
        with self.assertRaises(TypeError):
            my_dict(None)

    def test_dict_with_empty_string(self):
        self.assertTrue(my_dict({"a":""}))

    def test_dict_with_non_dict_value(self):
        with self.assertRaises(TypeError):
            my_dict({"a":[]})

    def test_dict_with_dict_value(self):
        with self.assertRaises(TypeError):
            my_dict({"a":{}})
