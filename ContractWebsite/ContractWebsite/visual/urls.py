from django.urls import path

from ContractWebsite.visual.views import ViewPage, MyLoginView, RegistrationView

urlpatterns=(
    path('',MyLoginView.as_view(),name="index"),
    path("r/",RegistrationView.as_view(),name="register" )
)