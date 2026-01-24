import unittest
from mbpp_712_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])

    def test_empty_list(self):
        self.assertEqual(remove_duplicate([]), [])

    def test_single_element(self):
        self.assertEqual(remove_duplicate([1]), [1])

    def test_duplicate_at_start(self):
        self.assertEqual(remove_duplicate([2, 2, 3, 3, 4]), [2, 3, 4])

    def test_duplicate_at_end(self):
        self.assertEqual(remove_duplicate([1, 1, 2, 2]), [1, 2])

    def test_duplicate_in_middle(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 2, 3]), [1, 2, 3])

    def test_duplicate_only(self):
        self.assertEqual(remove_duplicate([2, 2]), [2])

    def test_mixed_data_types(self):
        self.assertEqual(remove_duplicate([1, 'a', 2, 'a', 3]), [1, 'a', 3])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_duplicate(1.23)
