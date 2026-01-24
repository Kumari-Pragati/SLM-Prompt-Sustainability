import unittest
from mbpp_272_code import rear_extract

class TestRearExtract(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = [3, 6, 9]
        self.assertEqual(rear_extract(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = []
        self.assertEqual(rear_extract(test_list), expected_output)

    def test_single_element_list(self):
        test_list = [[1]]
        expected_output = [1]
        self.assertEqual(rear_extract(test_list), expected_output)

    def test_single_sublist(self):
        test_list = [1, 2, 3]
        expected_output = [3]
        self.assertEqual(rear_extract(test_list), expected_output)

    def test_error_handling(self):
        test_list = [1, 2, 3]
        with self.assertRaises(TypeError):
            rear_extract(test_list)
