import unittest
from mbpp_533_code import remove_datatype

class TestRemoveDatatype(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_datatype([], int), [])

    def test_single_element(self):
        self.assertEqual(remove_datatype([1], int), [1])
        self.assertEqual(remove_datatype([1.0], float), [1.0])
        self.assertEqual(remove_datatype(["1"], str), ["1"])

    def test_multiple_elements(self):
        self.assertEqual(remove_datatype([1, 2, 3], int), [2, 3])
        self.assertEqual(remove_datatype([1.0, 2.0, 3.0], float), [1, 3])
        self.assertEqual(remove_datatype(["1", "2", "3"], str), ["2"])

    def test_mixed_datatypes(self):
        self.assertEqual(remove_datatype([1, 1.0, "1", [1]], int), [1.0, "1", [1]])
        self.assertEqual(remove_datatype([1, 1.0, "1", [1]], float), [1])
        self.assertEqual(remove_datatype([1, 1.0, "1", [1]], str), [1, 1.0, [1]])

    def test_invalid_data_type(self):
        self.assertRaises(TypeError, remove_datatype, [1, 2, 3], "str")
        self.assertRaises(TypeError, remove_datatype, [1, 2, 3], 1)
