import unittest
from mbpp_90_code import len_log

class TestLenLog(unittest.TestCase):
    
    def test_typical_case(self):
        list1 = ['abc', 'defg', 'hij']
        self.assertEqual(len_log(list1), 4)

    def test_single_element_list(self):
        list1 = ['abc']
        self.assertEqual(len_log(list1), 3)

    def test_empty_list(self):
        list1 = []
        self.assertEqual(len_log(list1), 0)

    def test_longest_string_at_end(self):
        list1 = ['abc', 'def', 'ghijk']
        self.assertEqual(len_log(list1), 5)

    def test_longest_string_at_start(self):
        list1 = ['abcdefg', 'hi', 'j']
        self.assertEqual(len_log(list1), 7)

    def test_invalid_input(self):
        list1 = ['abc', 123, 'def']
        with self.assertRaises(TypeError):
            len_log(list1)
