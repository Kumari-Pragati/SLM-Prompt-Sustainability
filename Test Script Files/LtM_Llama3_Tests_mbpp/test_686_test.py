import unittest
from mbpp_686_code import freq_element

class TestFreqElement(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(freq_element(()), '({})')

    def test_single_element(self):
        self.assertEqual(freq_element((1,)), '({\'1\': 1})')

    def test_multiple_elements(self):
        self.assertEqual(freq_element((1, 2, 2, 3)), '({\'1\': 1, \'2\': 2, \'3\': 1})')

    def test_duplicates(self):
        self.assertEqual(freq_element((1, 2, 2, 2, 3)), '({\'1\': 1, \'2\': 3, \'3\': 1})')

    def test_empty_input_list(self):
        self.assertEqual(freq_element([]), '({})')

    def test_non_integer_input(self):
        self.assertEqual(freq_element(('a', 'b', 'a')), '({\'a\' : 2, \'b\' : 1})')

    def test_mixed_input(self):
        self.assertEqual(freq_element((1, 'a', 2, 'b', 2)), '({\'1\' : 1, \'a\' : 1, \'2\' : 2, \'b\' : 1})')
