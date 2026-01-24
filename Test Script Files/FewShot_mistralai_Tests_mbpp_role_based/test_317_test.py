import unittest
from mbpp_317_code import modified_encode

class TestModifiedEncode(unittest.TestCase):
    def test_single_element_list(self):
        self.assertEqual(modified_encode([1]), [1])
        self.assertEqual(modified_encode([0]), [0])
        self.assertEqual(modified_encode([-1]), [-1])

    def test_two_elements_list(self):
        self.assertEqual(modified_encode([1, 1]), [2, 1])
        self.assertEqual(modified_encode([0, 0]), [0, 0])
        self.assertEqual(modified_encode([-1, -1]), [-1, -1])

    def test_three_elements_list(self):
        self.assertEqual(modified_encode([1, 1, 1]), [3, 1])
        self.assertEqual(modified_encode([0, 0, 0]), [0, 0])
        self.assertEqual(modified_encode([-1, -1, -1]), [-1, -1])

    def test_multiple_groups_list(self):
        self.assertEqual(modified_encode([1, 2, 1, 2, 1]), [2, 1, 2, 1])
        self.assertEqual(modified_encode([0, 1, 0, 1, 0]), [2, 0, 2, 0])
        self.assertEqual(modified_encode([-1, 0, -1, 0, -1]), [-1, 0, -1, 0, -1])

    def test_empty_list(self):
        self.assertEqual(modified_encode([]), [])

    def test_list_with_non_numeric_elements(self):
        self.assertRaises(TypeError, modified_encode, ['a', 'b', 'c'])
        self.assertRaises(TypeError, modified_encode, [1, 'b', 2])
