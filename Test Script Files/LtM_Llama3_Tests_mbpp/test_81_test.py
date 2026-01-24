import unittest
from mbpp_81_code import zip_tuples

class TestZipTuples(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(zip_tuples([], []), [])

    def test_single_element_input(self):
        self.assertEqual(zip_tuples([1], [2]), [(1, 2)])

    def test_equal_length_input(self):
        self.assertEqual(zip_tuples([1, 2, 3], [4, 5, 6]), [(1, 4), (2, 5), (3, 6)])

    def test_unequal_length_input(self):
        self.assertEqual(zip_tuples([1, 2, 3, 4], [4, 5, 6]), [(1, 4), (2, 5), (3, 6)])

    def test_cyclic_input(self):
        self.assertEqual(zip_tuples([1, 2, 3], [4, 5, 6, 4]), [(1, 4), (2, 5), (3, 6)])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            zip_tuples('test', [1, 2, 3])
