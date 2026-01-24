import unittest
from mbpp_90_code import len_log

class TestLenLog(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = ['hello', 'world', 'unittest']
        self.assertEqual(len_log(list1), 6)

    def test_edge_condition(self):
        list1 = ['a']
        self.assertEqual(len_log(list1), 1)

    def test_boundary_condition(self):
        list1 = ['', 'b']
        self.assertEqual(len_log(list1), 1)

    def test_invalid_input(self):
        list1 = ['hello', 123, 'unittest']
        with self.assertRaises(TypeError):
            len_log(list1)
