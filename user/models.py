from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils.safestring import mark_safe


class UserProfile(models.Model):
    CITY = (
        ('Tashkent', 'Tashkent'),
        ('Andijon', 'Andijon'),
        ('Jizzah', 'Jizzah'),
        ('Xorazm', 'Xorazm'),

    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20, choices=CITY)
    country = models.CharField(blank=True, max_length=20)
    image = models.ImageField(blank=True, upload_to='images/users/')

    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + '[' + self.user.username + ']'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'