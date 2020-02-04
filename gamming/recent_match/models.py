from django.db import models
import random
import os

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

# Create your models here.


class RecentMatch(models.Model):
    match_name = models.CharField(max_length=120, null=True, blank=True)
    match_image = models.ImageField(upload_to=upload_image_path)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.match_name
