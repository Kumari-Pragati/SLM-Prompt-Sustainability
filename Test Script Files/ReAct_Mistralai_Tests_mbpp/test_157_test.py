import unittest
from mbpp_157_code import encode_list

class TestEncodeList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(encode_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(encode_list([1]), [[1, 1]])

    def test_duplicate_elements(self):
        self.assertEqual(encode_list([1, 1, 2, 2, 3]), [[2, 1], [2, 1], [1, 2], [1, 3]])

    def test_mixed_elements(self):
        self.assertEqual(encode_list([1, 'a', 1, 'a', 2]), [[2, 1], [2, 'a'], [1, 'a']])

    def test_list_with_only_one_group(self):
        self.assertEqual(encode_list([1, 2, 3, 4, 1]), [[1, 1], [1, 2], [1, 3], [1, 4]])

    def test_list_with_multiple_groups(self):
        self.assertEqual(encode_list([1, 2, 1, 2, 1, 2, 3]), [[2, 1], [2, 1], [1, 2], [2, 3]])

    def test_list_with_empty_group(self):
        self.assertEqual(encode_list([1, 2, 3, [], 1]), [[1, 1], [1, 2], [1, 3], [], [1, 1]])

    def test_list_with_only_empty_group(self):
        self.assertEqual(encode_list([[], 1, 2]), [[1, []], [1, []], [1, 2]])

    def test_list_with_negative_numbers(self):
        self.assertEqual(encode_list([1, -1, 2, -1]), [[2, 1], [1, -1], [1, 2], [1, -1]])

    def test_list_with_floats(self):
        self.assertEqual(encode_list([1.0, 2.0, 1.0]), [[1, 1.0], [1, 2.0], [1, 1.0]])

    def test_list_with_strings(self):
        self.assertEqual(encode_list(['a', 'b', 'a']), [[2, 'a'], [1, 'b'], [1, 'a']])

    def test_list_with_mixed_types(self):
        self.assertEqual(encode_list([1, 'a', 2.0, 'b']), [[1, 1], [1, 'a'], [1, 2.0], [1, 'b']])
