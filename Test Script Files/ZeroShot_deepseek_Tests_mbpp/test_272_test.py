import unittest
from mbpp_272_code import rear_extract

class TestRearExtract(unittest.TestCase):

    def test_rear_extract_positive(self):
        self.assertEqual(rear_extract([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [3, 6, 9])

    def test_rear_extract_negative(self):
        self.assertEqual(rear_extract([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), [-3, -6, -9])

    def test_rear_extract_mixed(self):
        self.assertEqual(rear_extract([[1, -2, 3], [-4, 5, -6], [7, -8, 9]]), [3, -6, 9])

    def test_rear_extract_empty(self):
        self.assertEqual(rear_extract([]), [])

    def test_rear_extract_single_element(self):
        self.assertEqual(rear_extract([[1]]), [1])

    def test_rear_extract_single_list(self):
        self.assertEqual(rear_extract([[1, 2, 3]]), [3])
