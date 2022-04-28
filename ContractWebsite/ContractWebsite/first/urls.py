from django.urls import path

from ContractWebsite.first.views import AllNoticeView, NoticeListView

urlpatterns=(
    path('b/',AllNoticeView.as_view(),name="all notice"),
    path('a/',NoticeListView.as_view(),name="filter"),
    #path('b/',AllNoticeView.as_view(),name="filter"),
)