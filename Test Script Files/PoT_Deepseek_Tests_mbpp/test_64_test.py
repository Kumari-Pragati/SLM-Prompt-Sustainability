import unittest
from mbpp_64_code import subject_marks

class TestSubjectMarks(unittest.TestCase):

    def test_typical_case(self):
        subjectmarks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        expected_output = [('Science', 90), ('Maths', 97), ('English', 88), ('Social sciences', 82)]
        self.assertEqual(subject_marks(subjectmarks), expected_output)

    def test_empty_list(self):
        subjectmarks = []
        expected_output = []
        self.assertEqual(subject_marks(subjectmarks), expected_output)

    def test_single_subject(self):
        subjectmarks = [('Maths', 97)]
        expected_output = [('Maths', 97)]
        self.assertEqual(subject_marks(subjectmarks), expected_output)

    def test_duplicate_marks(self):
        subjectmarks = [('English', 88), ('Science', 88), ('Maths', 88), ('Social sciences', 88)]
        expected_output = [('Maths', 88), ('Science', 88), ('English', 88), ('Social sciences', 88)]
        self.assertEqual(subject_marks(subjectmarks), expected_output)

    def test_negative_marks(self):
        subjectmarks = [('English', -88), ('Science', -90), ('Maths', -97), ('Social sciences', -82)]
        expected_output = [('Maths', -97), ('Science', -90), ('English', -88), ('Social sciences', -82)]
        self.assertEqual(subject_marks(subjectmarks), expected_output)
