import unittest
from mbpp_495_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):

    def test_remove_lowercase_typical_case(self):
        self.assertEqual(remove_lowercase('HelloWorld'), 'HW')

    def test_remove_lowercase_edge_case(self):
        self.assertEqual(remove_lowercase(''), '')
        self.assertEqual(remove_lowercase('1234567890'), '1234567890')
        self.assertEqual(remove_lowercase('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), '')

    def test_remove_lowercase_error_cases(self):
        with self.assertRaises(TypeError):
            remove_lowercase(12345)
        with self.assertRaises(TypeError):
            remove_lowercase(None)
        with self.assertRaises(TypeError):
            remove_lowercase(['Hello', 'World'])
