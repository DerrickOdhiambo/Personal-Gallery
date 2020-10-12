from django.db import models
import datetime as dt


class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class Image(models.Model):
    image = models.ImageField(upload_to='index/')
    image_name = models.CharField(max_length=150)
    image_description = models.CharField(max_length=200)
    location = models.ForeignKey(Location,
                                 on_delete=models.CASCADE, null=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def delete_image(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def search_image_by_category(cls, image_category):
        images = cls.objects.filter(category__name__icontains=image_category)
        return images

    @classmethod
    def filter_by_location(cls, location_id):
        images = cls.objects.filter(location__id=location_id)
        return images
