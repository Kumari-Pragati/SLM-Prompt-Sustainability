import unittest
from mbpp_290_code import max_length

class TestMaxLength(unittest.TestCase):

    def test_max_length(self):
        self.assertEqual(max_length(['apple', 'banana', 'cherry']), (9, 'cherry'))

    def test_max_length_empty_list(self):
        self.assertEqual(max_length([]), (0, None))

    def test_max_length_single_element(self):
        self.assertEqual(max_length(['hello']), (5, 'hello'))

    def test_max_length_multiple_elements(self):
        self.assertEqual(max_length(['apple', 'banana', 'cherry', 'date']), (6, 'date'))

    def test_max_length_all_elements_equal(self):
        self.assertEqual(max_length(['apple', 'banana', 'cherry', 'date', 'elder']), (6, 'elder'))
