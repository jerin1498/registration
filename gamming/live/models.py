
import random
import os
from django.db import models


# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )


class LiveQuerySet(models.query.QuerySet):
    def by_name(self, name):
        return self.filter(name=name)


class LiveModelManager(models.Manager):
    def get_query_set(self):
        return LiveQuerySet(self.model, using=self._db)

    def by_name(self, name):
        return self.get_query_set().by_name(name)


class Live(models.Model):
    name = models.CharField(max_length=120, default='links')
    owner_name = models.CharField(max_length=120, default='Abishon RT')
    owner_profile_pic  = models.ImageField(null=True, blank=True)
    owner_contact_number = models.PositiveIntegerField(null=True, blank=True)
    owner_instagram_link = models.URLField(null=True, blank=True)
    manager_name = models.CharField(max_length=120, default='Shibu Rbz')
    manager_profile_pic = models.ImageField(null=True, blank=True)
    manager_contact_number = models.PositiveIntegerField(null=True, blank=True)
    manager_instagram_link = models.URLField(null=True, blank=True)
    madpyrate_link = models.URLField(null=True, blank=True)
    madpyrate_fb_link = models.URLField(null=True, blank=True)
    madpyrate_twiter_link = models.URLField(null=True, blank=True)
    youtube_link = models.URLField(null=True, blank=True)
    whats_app_group_link = models.URLField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    registration = models.BooleanField(default=False)
    youtube_live = models.BooleanField(default=False)
    display_messages_1 = models.CharField(max_length=1000, null=True, blank=True)
    display_messages_2 = models.CharField(max_length=1000, null=True, blank=True)
    display_messages_3 = models.CharField(max_length=1000, null=True, blank=True)

    objects = LiveModelManager()

    def __str__(self):
        return self.name
