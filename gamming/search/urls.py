from django.conf.urls import url

from .views import (
        SearchTeamView
        )

urlpatterns = [
    url(r'^$', SearchTeamView.as_view(), name='query'),
]

