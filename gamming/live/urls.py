from django.conf.urls import url

from .views import (
       live,
        account,
        )

urlpatterns = [
    url(r'^$', live, name='youtube'),
    url(r'^account/', account, name='account'),
]

