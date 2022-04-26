from django.urls import path

from ContractWebsite.first.views import AllNoticeView

urlpatterns=(
    path('',AllNoticeView.as_view(),name="all notice"),
)