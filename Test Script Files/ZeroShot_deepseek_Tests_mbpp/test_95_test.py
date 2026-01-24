import unittest
from mbpp_95_code import Find_Min_Length

class TestFindMinLength(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(Find_Min_Length([]), 0)

    def test_single_element_list(self):
        self.assertEqual(Find_Min_Length(['hello']), 5)

    def test_multiple_elements_list(self):
        self.assertEqual(Find_Min_Length(['hello', 'world', 'python']), 5)
        self.assertEqual(Find_Min_Length(['hello', 'world', 'programming']), 7)

    def test_list_with_empty_string(self):
        self.assertEqual(Find_Min_Length(['hello', 'world', '']), 0)

    def test_list_with_numbers(self):
        self.assertEqual(Find_Min_Length(['123', '456', '789']), 3)

    def test_list_with_mixed_types(self):
        with self.assertRaises(TypeError):
            Find_Min_Length(['hello', 123, 'world'])
