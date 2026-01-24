import unittest
from mbpp_321_code import find_demlo

class TestFindDemlo(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_demlo("demlo"), "1234")

    def test_empty_string(self):
        self.assertEqual(find_demlo(""), "")

    def test_single_character(self):
        self.assertEqual(find_demlo("a"), "1")

    def test_long_string(self):
        self.assertEqual(find_demlo("demlo"*1000), "1234"*1000)

    def test_string_with_special_characters(self):
        self.assertEqual(find_demlo("demlo!@#"), "1234567891011121314")

    def test_string_with_spaces(self):
        self.assertEqual(find_demlo("dem lo"), "123456")
