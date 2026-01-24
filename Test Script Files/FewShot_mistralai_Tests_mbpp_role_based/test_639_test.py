import unittest
from mbpp_639_code import sample_nam

class TestSampleNam(unittest.TestCase):
    def test_valid_uppercase_and_lowercase(self):
        self.assertEqual(sample_nam(["JohnDoe", "janeSmith"]), 2)

    def test_empty_list(self):
        self.assertEqual(sample_nam([]), 0)

    def test_mixed_case(self):
        self.assertEqual(sample_nam(["John_Doe", "Jane_Smith"]), 0)

    def test_all_uppercase(self):
        self.assertEqual(sample_nam(["JOHNDOE", "JANESMITH"]), 0)

    def test_all_lowercase(self):
        self.assertEqual(sample_nam(["johndoe", "janesmith"]), 0)

    def test_invalid_input(self):
        self.assertRaises(TypeError, sample_nam, [1, 2, 3])
