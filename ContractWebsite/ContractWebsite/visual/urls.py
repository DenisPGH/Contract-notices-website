from django.urls import path

from ContractWebsite.visual.views import ViewPage

urlpatterns=(
    path('',ViewPage.as_view(),name="index"),
)