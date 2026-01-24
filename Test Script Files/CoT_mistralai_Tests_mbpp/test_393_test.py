import unittest
from mbpp_393_code import max_length_list

class TestMaxLengthList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_length_list([]), (0, []))

    def test_single_element_list(self):
        for element in ['a', [1], (1, 2), 1]:
            self.assertEqual(max_length_list([element]), (len(element), element))

    def test_multiple_elements(self):
        test_list = [['abc', 'def', 'ghi'], [1, 2, 3], (1, 2, 3), [1, 2, 3, 4], [1, 2, 3, 4, 5]]
        expected_length = max(map(len, test_list))
        expected_max_list = max(test_list, key=len)
        self.assertEqual(max_length_list(test_list), (expected_length, expected_max_list))

    def test_mixed_types(self):
        test_list = ['abc', 1, [1, 2, 3], (1, 2, 3), [1, 2, 3, 4], [1, 2, 3, 4, 5]]
        self.assertEqual(max_length_list(test_list), (3, ['abc']))

    def test_invalid_input(self):
        self.assertRaises(TypeError, max_length_list, (1, 2, 3))
