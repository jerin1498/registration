from django.conf.urls import url




from .views import (
                        RegisterVew,
                        TeamList,
                        TeamDetail,
                        MatchDate,
                        VerifiedTeams,
                        ContactPage,
                        QualifiedTeams,
                        RegisteredTeams,
                        about,
                        PortFolio,
                        Home,
                        maps,

                        )

urlpatterns = [

    url("^$", Home.as_view(), name='home'),
    url(r"^register/", RegisterVew.as_view(), name='register'),
    url(r"^about/", about, name='about'),
    url(r"^teamlist/", TeamList.as_view(), name='team-list'),
    url(r'^detail/(?P<slug>[\w-]+)/$', TeamDetail.as_view(), name='team-detail'),
    url(r"^matchdate/", MatchDate.as_view(), name='match-date'),
    url(r"^verifiedteams/", VerifiedTeams.as_view(), name='verified-teams'),
    url(r"^qualifiedteams/", QualifiedTeams.as_view(), name='qualified-teams'),
    url(r"^contact/", ContactPage.as_view(), name='contact'),
    url(r"^registeredteams/", RegisteredTeams.as_view(), name='registered-teams'),
    url(r"^portfolio/", PortFolio.as_view(), name='portfolio'),
    url(r"^maps/", maps, name='maps'),

    ]
