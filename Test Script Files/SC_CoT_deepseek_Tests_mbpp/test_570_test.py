import unittest
from mbpp_570_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_typical_case(self):
        list1 = ["Hello world", "Python is fun"]
        charlist = ["world", "fun"]
        expected_output = ["Hello ", "Python is "]
        self.assertEqual(remove_words(list1, charlist), expected_output)

    def test_edge_case(self):
        list1 = ["   ", ""]
        charlist = [" "]
        expected_output = ["", ""]
        self.assertEqual(remove_words(list1, charlist), expected_output)

    def test_corner_case(self):
        list1 = ["Hello world", "world is here"]
        charlist = ["world"]
        expected_output = ["Hello ", " "]
        self.assertEqual(remove_words(list1, charlist), expected_output)

    def test_invalid_input(self):
        list1 = ["Hello world", "Python is fun"]
        charlist = ["world", 123]
        with self.assertRaises(TypeError):
            remove_words(list1, charlist)
