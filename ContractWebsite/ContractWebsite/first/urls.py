from django.urls import path

from ContractWebsite.first.views import AllNoticeView, NoticeListView

urlpatterns=(
    path('',AllNoticeView.as_view(),name="all notice"),
    path('a/',NoticeListView.as_view(),name="filter"),
)