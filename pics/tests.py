from django.test import TestCase
from .models import Image, Category, Location


class ImageTestCase(TestCase):

    def setUp(self):
        self.new_image = Image(
            image_description='Test description', image_name='Family', image='image/path')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))
