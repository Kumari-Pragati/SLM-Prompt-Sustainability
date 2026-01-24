import unittest
from mbpp_272_code import rear_extract

class TestRearExtract(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(rear_extract([1, 2, 3]), [3])
        self.assertEqual(rear_extract([4, 5, 6]), [6])

    def test_empty_list(self):
        self.assertEqual(rear_extract([]), [])

    def test_single_element_list(self):
        self.assertEqual(rear_extract([4]), [4])

    def test_negative_numbers(self):
        self.assertEqual(rear_extract([-1, -2, -3]), [-3])
        self.assertEqual(rear_extract([-4, -5, -6]), [-6])

    def test_mixed_types(self):
        self.assertEqual(rear_extract([1, 2, 3, 'x']), [3])
        self.assertEqual(rear_extract(['a', 1, 2]), ['2'])

    def test_nested_lists(self):
        self.assertEqual(rear_extract([[1, 2], [3, 4]]), [4])
        self.assertEqual(rear_extract([[1], [2], [3]]), [3])
