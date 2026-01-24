import unittest
from mbpp_513_code import add_str

class TestAddStr(unittest.TestCase):

    def test_add_str(self):
        self.assertEqual(add_str([1, 2], 3), [1, 2, 3])
        self.assertEqual(add_str([1, 2, 3], 4), [1, 2, 3, 4])
        self.assertEqual(add_str([1, 2, 3, 4], 5), [1, 2, 3, 4, 5])
        self.assertEqual(add_str([], 6), [6])
        self.assertEqual(add_str([1], 2), [1, 2])
        self.assertEqual(add_str([1, 2, 3], 0), [1, 2, 3])
        self.assertEqual(add_str([], 0), [])

    def test_add_str_type_error(self):
        with self.assertRaises(TypeError):
            add_str('test', 1)

    def test_add_str_value_error(self):
        with self.assertRaises(ValueError):
            add_str([1, 2, 3], 'test')
