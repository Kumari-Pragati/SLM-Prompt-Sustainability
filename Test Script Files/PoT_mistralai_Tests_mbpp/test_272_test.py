import unittest
from mbpp_272_code import rear_extract

class TestRearExtract(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(rear_extract([[1, 2, 3], [4, 5], [6, 7, 8]]), [3, 5, 8])
        self.assertEqual(rear_extract([[1], [2], [3]])), [3, 2, 1]
        self.assertEqual(rear_extract([[1, 2], [3], [4, 5]]), [5, 3])

    def test_edge_case_empty_list(self):
        self.assertListEqual(rear_extract([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(rear_extract([[1]]), [1])

    def test_edge_case_single_element_sublist(self):
        self.assertEqual(rear_extract([[1], [2]]), [2])
