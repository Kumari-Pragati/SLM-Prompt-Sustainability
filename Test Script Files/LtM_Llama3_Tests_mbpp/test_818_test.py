import unittest
from mbpp_818_code import lower_ctr

class TestLowerCtr(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(lower_ctr(""), 0)

    def test_all_lowercase(self):
        self.assertEqual(lower_ctr("hello"), 5)

    def test_mixed_case(self):
        self.assertEqual(lower_ctr("HeLlO"), 3)

    def test_all_uppercase(self):
        self.assertEqual(lower_ctr("HELLO"), 0)

    def test_non_alpha_characters(self):
        self.assertEqual(lower_ctr("Hello123"), 3)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            lower_ctr(123)
