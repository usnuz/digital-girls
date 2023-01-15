from django.db import models
from django.core.validators import FileExtensionValidator, ValidationError
# from location_field.models.plain import PlainLocationField


class Slider(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    img = models.ImageField(upload_to='media/slider/')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    img = models.ImageField(upload_to='slider/')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.title is not None:
            return self.title
        else:
            return self.body


def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.png']
    if not ext in valid_extensions:
        raise ValidationError(u'File not supported!\nonly .png')


class Direction(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(validators=[validate_file_extension], upload_to='icon/direction/')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Registration(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField()
    mail = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    tel = models.CharField(max_length=255, unique=True)
    is_checked = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Result(models.Model):
    item = models.ManyToManyField('ResultItem')
    title = models.CharField(max_length=255, default='Results')
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ResultItem(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(validators=[validate_file_extension], upload_to='icon/results/')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    url = models.URLField()
    tel = models.CharField(max_length=255)
    mail = models.EmailField()
    address = models.CharField(max_length=255)
    longitude = models.FloatField(default=40.747404)
    latitude = models.FloatField(default=72.359645)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Girls in Digital'


