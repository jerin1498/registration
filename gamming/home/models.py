from django.db import models
from gamming.utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse
import random
import os
from django.db import models
from django.db.models import Q



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


class RegistrationQuerySet(models.query.QuerySet):
    def verified(self):
        return self.filter(verified=True)

    def qualified(self):
        return self.filter(qualified=True, verified=True)

    def match_day_1(self):
        return self.filter(verified=True, match_day=1)

    def match_day_2(self):
        return self.filter(verified=True, match_day=2)

    def match_day_3(self):
        return self.filter(verified=True, match_day=3)

    def match_day_4(self):
        return self.filter(verified=True, match_day=4)

    def match_day_5(self):
        return self.filter(verified=True, match_day=5)

    def match_day_6(self):
        return self.filter(verified=True, match_day=6)

    def match_day_7(self):
        return self.filter(verified=True, match_day=7)

    def match_day_8(self):
        return self.filter(verified=True, match_day=8)

    def match_day_9(self):
        return self.filter(verified=True, match_day=9)

    def match_day_10(self):
        return self.filter(verified=True, match_day=10)

    def semi_final_match(self):
        return self.filter(verified=True, semi_final_match=True)

    def final_match(self):
        return self.filter(verified=True, final_match=True)



    def search(self, query):
        lookups = (Q(team_name__icontains=query) |
                  Q(player_1__icontains=query) |
                  Q(player_1_pubg_id__icontains=query) |
                   Q(player_2__icontains=query) |
                   Q(player_2_pubg_id__icontains=query) |
                   Q(player_3__icontains=query) |
                   Q(player_3_pubg_id__icontains=query) |
                   Q(player_4__icontains=query) |
                   Q(player_4_pubg_id__icontains=query) |
                  Q(team_position__icontains=query)

                  )
        # tshirt, t-shirt, t shirt, red, green, blue,
        return self.filter(lookups).distinct()


    def player_exists(self, query):
        lookups = (
                   Q(player_1__exact=query) |

                   Q(player_2__exact=query) |

                   Q(player_3__exact=query) |

                   Q(player_4__exact=query)

                   )

        return self.filter(lookups).distinct()

    def player_id_exists(self, query):
        lookups = (

                   Q(player_1_pubg_id__exact=query) |

                   Q(player_2_pubg_id__exact=query) |

                   Q(player_3_pubg_id__exact=query) |

                   Q(player_4_pubg_id__exact=query)

                   )

        return self.filter(lookups).distinct()




class RegistrationManager(models.Manager):
    def get_queryset(self):
        return RegistrationQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def verified(self):
        return self.get_queryset().verified()

    def qualified(self):
        return self.get_queryset().qualified()

    def match_day_1(self):
        return self.get_queryset().match_day_1()

    def match_day_2(self):
        return self.get_queryset().match_day_2()

    def match_day_3(self):
        return self.get_queryset().match_day_3()

    def match_day_4(self):
        return self.get_queryset().match_day_4()

    def match_day_5(self):
        return self.get_queryset().match_day_5()

    def match_day_6(self):
        return self.get_queryset().match_day_6()

    def match_day_7(self):
        return self.get_queryset().match_day_7()

    def match_day_8(self):
        return self.get_queryset().match_day_8()

    def match_day_9(self):
        return self.get_queryset().match_day_9()


    def match_day_10(self):
        return self.get_queryset().match_day_9()

    def semi_final_match(self):
        return self.get_queryset().semi_final_match()

    def final_match(self):
        return self.get_queryset().final_match()

    def player_exists(self, query):

        return self.get_queryset().player_exists(query)

    def id_exists(self, query):
        return self.get_queryset().player_id_exists(query)


    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None


    def search(self, query):
        return self.get_queryset().search(query)


class Registration(models.Model):
    team_name = models.CharField(max_length=120, unique=True)
    team_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    contact_number = models.IntegerField(blank=True, null=True, unique=True)
    team_position = models.PositiveIntegerField(null=True, blank=True)
    player_1 = models.CharField(max_length=120, unique=True)
    player_1_pubg_id = models.IntegerField(unique=True)
    player_2 = models.CharField(max_length=120, unique=True)
    player_2_pubg_id = models.IntegerField(unique=True)
    player_3 = models.CharField(max_length=120, unique=True)
    player_3_pubg_id = models.IntegerField(unique=True)
    player_4 = models.CharField(max_length=120, unique=True)
    player_4_pubg_id = models.IntegerField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)
    verified = models.BooleanField(default=False)
    qualified = models.BooleanField(default=False)
    semi_final_match = models.BooleanField(default=False)
    final_match = models.BooleanField(default=False)
    match_day = models.PositiveIntegerField(null=True, blank=True)


    objects = RegistrationManager()
#safasdf

    def __str__(self):
        return self.team_name

    def get_absolute_url(self):
        return reverse("home:team-detail", kwargs={"slug": self.slug})


def pre_save_registration(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_registration, sender=Registration)

