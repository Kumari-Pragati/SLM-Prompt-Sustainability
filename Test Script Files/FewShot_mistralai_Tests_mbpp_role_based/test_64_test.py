import unittest
from mbpp_64_code import subject_marks

class TestSubjectMarks(unittest.TestCase):
    def test_sorted_marks(self):
        subjectmarks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        expected = [('Maths', 97), ('Science', 90), ('English', 88), ('Social sciences', 82)]
        self.assertEqual(subject_marks(subjectmarks), expected)

    def test_empty_list(self):
        self.assertEqual(subject_marks([]), [])

    def test_single_subject(self):
        self.assertEqual(subject_marks([('Subject', 100)]), [('Subject', 100)])

    def test_duplicate_subjects(self):
        self.assertEqual(subject_marks([('Subject1', 100), ('Subject1', 99)]), [('Subject1', 100)])

    def test_negative_marks(self):
        self.assertEqual(subject_marks([('Subject', -1)]), [('Subject', -1)])
