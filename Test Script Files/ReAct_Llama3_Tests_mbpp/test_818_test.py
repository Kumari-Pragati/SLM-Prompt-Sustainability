import unittest
from mbpp_818_code import lower_ctr

class TestLowerCtR(unittest.TestCase):
    def test_lower_ctr_typical(self):
        self.assertEqual(lower_ctr("hello"), 2)

    def test_lower_ctr_empty(self):
        self.assertEqual(lower_ctr(""), 0)

    def test_lower_ctr_all_lower(self):
        self.assertEqual(lower_ctr("abcdefghijklmnopqrstuvwxyz"), 26)

    def test_lower_ctr_all_upper(self):
        self.assertEqual(lower_ctr("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 0)

    def test_lower_ctr_mixed(self):
        self.assertEqual(lower_ctr("HelloWorld"), 2)

    def test_lower_ctr_non_ascii(self):
        self.assertEqual(lower_ctr("hëllo"), 3)

    def test_lower_ctr_non_string(self):
        with self.assertRaises(TypeError):
            lower_ctr(123)
