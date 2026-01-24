import unittest
from mbpp_64_code import subject_marks

class TestSubjectMarks(unittest.TestCase):

    def test_subject_marks(self):
        subjectmarks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        expected_output = [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
        self.assertEqual(subject_marks(subjectmarks), expected_output)

    def test_empty_list(self):
        subjectmarks = []
        expected_output = []
        self.assertEqual(subject_marks(subjectmarks), expected_output)

    def test_single_element(self):
        subjectmarks = [('Maths', 97)]
        expected_output = [('Maths', 97)]
        self.assertEqual(subject_marks(subjectmarks), expected_output)

    def test_duplicate_marks(self):
        subjectmarks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 97)]
        expected_output = [('Social sciences', 97), ('Maths', 97), ('Science', 90), ('English', 88)]
        self.assertEqual(subject_marks(subjectmarks), expected_output)
