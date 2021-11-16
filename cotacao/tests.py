from django.test import TestCase
from .models import Post
from django.db import models as django_models

# Create your tests here.
class Post(TestCase):
    def setUp(self):
        base = Post.objects.get_field_by_name('dt_vl')
        self.assertIsInstance(base, django_models.DateField)
        self.assertEquals(4,base.max_length)