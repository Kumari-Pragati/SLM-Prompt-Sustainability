import unittest
from mbpp_639_code import sample_nam

class TestSampleNam(unittest.TestCase):

    def test_simple_uppercase_and_lowercase(self):
        self.assertEqual(sample_nam(["John", "jim", "SARA"]), 3)

    def test_empty_list(self):
        self.assertEqual(sample_nam([]), 0)

    def test_all_uppercase(self):
        self.assertEqual(sample_nam(["JOHN", "JIM"]), 0)

    def test_all_lowercase(self):
        self.assertEqual(sample_nam(["john", "jim"]), 0)

    def test_mixed_case(self):
        self.assertEqual(sample_nam(["John_1", "jim_2", "SARA_3"]), 3)

    def test_special_characters(self):
        self.assertEqual(sample_nam(["John#1", "jim@2", "SARA$3"]), 0)

    def test_numbers(self):
        self.assertEqual(sample_nam(["John1", "jim2", "SARA3"]), 0)
