from django.urls import path
from rest_framework.schemas import get_schema_view

from ContractWebsite.first.views import AllNoticeView, NoticeListView

urlpatterns=(
    path('b/',AllNoticeView.as_view(),name="all notice"),
    path('filter/',NoticeListView.as_view(),name="filter"),
    path('schema/', get_schema_view(
        title="TEST JSON Schema",
        description="first steps in JSON schema",
        version="1.0.0"
    ), name='openapi-schema'),
    #path('b/',AllNoticeView.as_view(),name="filter"),
)