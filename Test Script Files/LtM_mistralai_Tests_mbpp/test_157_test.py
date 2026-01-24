import unittest
from mbpp_157_code import islice
from 157_code import encode_list

class TestEncodeList(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(encode_list([1, 1, 2, 3, 3, 4]), [
            [1, 1],
            [2, 2],
            [1, 3],
            [1, 4]
        ])

    def test_single_element_list(self):
        self.assertEqual(encode_list([1]), [
            [1, 1]
        ])

    def test_empty_list(self):
        self.assertEqual(encode_list([]), [])

    def test_list_with_duplicates_and_non_duplicates(self):
        self.assertEqual(encode_list([1, 2, 1, 3, 2, 1, 4]), [
            [1, 1],
            [1, 2],
            [1, 1],
            [1, 3],
            [2, 2],
            [1, 1],
            [1, 4]
        ])

    def test_list_with_long_sequences(self):
        self.assertEqual(encode_list(list(islice(range(100), 10))), [
            [10, 0],
            [10, 1],
            [10, 2],
            [10, 3],
            [10, 4],
            [10, 5],
            [10, 6],
            [10, 7],
            [10, 8],
            [10, 9]
        ])
