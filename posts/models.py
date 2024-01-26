from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse
from hitcount.models import HitCount


class Post(models.Model):
    ADMIN_ALLOWING_CHOICES = [
        ("allowed", "ALLOWED"),
        ("not_allowed", "NOT_ALLOWED")
    ]

    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    photo = models.ImageField(default='default_post_pic.jpg', upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_p',
                                        related_query_name='hit_count_generic_relation')

    admin_allowed = models.CharField(choices=ADMIN_ALLOWING_CHOICES, max_length=11, default="not_allowed")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.id})
