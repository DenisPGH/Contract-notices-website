from django.urls import path

from ContractWebsite.visual.views import MyLoginView, RegistrationView, LogedPage, AdminsPage, delete_user, Back, \
    LogoutPageView, EditUsers

urlpatterns=(
    path('',MyLoginView.as_view(),name="index"),
    path("register/",RegistrationView.as_view(),name="register" ),
    path("loggedin/", LogedPage.as_view(), name="logged"),
    path("adm/", AdminsPage.as_view(), name="admins"),
    path("del/<int:pk>/",delete_user, name="delete user"),
    path("back/",Back.as_view(), name="back"),
    path("logout/",LogoutPageView.as_view(), name="logout"),
    path("edit/<int:pk>/",EditUsers.as_view(), name="edit user"),
)