import unittest
from mbpp_461_code import upper_ctr

class TestUpperCtr(unittest.TestCase):

    def test_upper_ctr_typical(self):
        self.assertEqual(upper_ctr("HelloWorld"), 2)

    def test_upper_ctr_edge(self):
        self.assertEqual(upper_ctr("ABC123"), 3)

    def test_upper_ctr_empty(self):
        self.assertEqual(upper_ctr(""), 0)

    def test_upper_ctr_all_lower(self):
        self.assertEqual(upper_ctr("hello"), 0)

    def test_upper_ctr_all_upper(self):
        self.assertEqual(upper_ctr("HELLO"), 5)

    def test_upper_ctr_mixed(self):
        self.assertEqual(upper_ctr("HeLlO"), 3)

    def test_upper_ctr_non_string(self):
        with self.assertRaises(TypeError):
            upper_ctr(123)

    def test_upper_ctr_non_ascii(self):
        self.assertEqual(upper_ctr("HéLlO"), 3)
