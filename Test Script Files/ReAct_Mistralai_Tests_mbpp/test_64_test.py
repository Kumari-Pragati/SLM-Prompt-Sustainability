import unittest
from mbpp_64_code import subject_marks

class TestSubjectMarks(unittest.TestCase):

    def test_sorted_marks(self):
        data = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        expected = [('Maths', 97), ('Science', 90), ('English', 88), ('Social sciences', 82)]
        self.assertEqual(subject_marks(data), expected)

    def test_same_marks(self):
        data = [('English', 88), ('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        expected = [('English', 88), ('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        self.assertEqual(subject_marks(data), expected)

    def test_empty_list(self):
        data = []
        expected = []
        self.assertEqual(subject_marks(data), expected)

    def test_single_subject(self):
        data = [('English', 88)]
        expected = [('English', 88)]
        self.assertEqual(subject_marks(data), expected)

    def test_negative_marks(self):
        data = [('English', -10), ('Science', 0)]
        expected = [('English', -10), ('Science', 0)]
        self.assertEqual(subject_marks(data), expected)

    def test_non_numeric_marks(self):
        data = [('English', 'a'), ('Science', 90)]
        with self.assertRaises(TypeError):
            subject_marks(data)
