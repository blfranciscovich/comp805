from django.test import TestCase
from .models import Education, Experience, Resume
import unittest

# Create your tests here.
class TestResume (TestCase):

    def setUp(self):
        self.resume.save()
        self.education.save()
        self.experience.save()

    def test_get_full_name(self):
        """
        Tests models.get_full_name(self):
        """
        expected = 'Bridget Franciscovich'
        self.assertEqual(self.resume.get_full_name(), expected)

    def test_get_last_name_first_name(self):
        """
        Tests models.get_last_first_name(self):
        """
        expected = 'Franciscovich, Bridget'
        self.assertEqual(self.resume.test_get_last_name_first_name(), expected)

    def test_get_education(self):
        """
        Tests models.get_education(self):
        """
        expected = self.education_set.all()
        self.assertEqual(self.resume.get_education().first(), expected)

    def test_get_experience(self):
        """
        Tests models.get_experience(self):
        """
        expected = list(experience.experience_set.all())
        self.assertEqual(self.resume.get_experience().first(), expected)

if __name__ == '__main__':
    try:
        import models
        print("models.py module found.Testing...")
        unittest.main( )
    except ImportError:
        print("Missing models.py module")
