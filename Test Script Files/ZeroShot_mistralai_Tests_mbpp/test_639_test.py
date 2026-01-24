import unittest
from mbpp_639_code import sample_nam

class TestSampleNam(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sample_nam([]), 0)

    def test_single_name(self):
        self.assertEqual(sample_nam(["ABC", "def"]), 3)
        self.assertEqual(sample_nam(["abc", "DEF"]), 0)
        self.assertEqual(sample_nam(["AbC", "dEf"]), 3)

    def test_multiple_names(self):
        self.assertEqual(sample_nam(["ABC", "abc", "Def", "def"]), 6)
        self.assertEqual(sample_nam(["AbC", "abc", "Def", "def"]), 6)
        self.assertEqual(sample_nam(["ABC", "abc", "AbC", "abc"]), 6)
