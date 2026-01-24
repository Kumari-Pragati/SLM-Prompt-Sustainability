import unittest
from mbpp_500_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(concatenate_elements([]), '')

    def test_single_element(self):
        self.assertEqual(concatenate_elements(['a']), ' a')

    def test_multiple_elements(self):
        self.assertEqual(concatenate_elements(['a', 'b', 'c']), ' a b c')

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            concatenate_elements([1, 'a'])

    def test_list_with_none(self):
        self.assertEqual(concatenate_elements([None, 'a']), ' None a')
