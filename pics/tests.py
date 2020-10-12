from django.test import TestCase
from .models import Image, Category, Location


class ImageTestCase(TestCase):

    def setUp(self):
        # new location
        self.new_location = Location(location_name='Kenya')
        self.new_location.save_location()

        # Creating a new category and saving it
        self.new_category = Category(category_name='Travel')
        self.new_category.save_category()

        self.new_image = Image(
            image_description='Test description', image_name='Family', image='image/path', location=self.new_location)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_image(self):
        self.new_image.save_image()
        self.new_image = Image.objects.all()
        self.assertTrue(len(self.new_image) > 0)

    def test_get_image_by_id(self):
        self.new_image.save_image()
        self.new_image = Image.get_image_by_id(1)
        self.assertTrue(isinstance(self.new_image, Image))

    def test_delete_image(self):
        Image.delete_image(self.new_image.id)
        images = Image.all_images()
        self.assertTrue(len(images) == 0)
