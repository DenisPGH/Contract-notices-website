from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics as api_views,permissions
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import filters
from django_filters import rest_framework as filters_rest
from django import forms
from django_filters import filters as filters_django
import datetime
from bootstrap_datepicker_plus.widgets import DatePickerInput
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
from rest_framework.response import Response

from ContractWebsite.first.models import Notice

class MyDateFilter(filters_rest.filters.DateFilter):
    date = filters_rest.DateFromToRangeFilter()


    # class Meta:
    #     model = Notice
    #     fields = ['id','date','tender_name']

class SearchSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField()
    class Meta:
        model = Notice
        fields = ('id','date','tender_name')


class FormSearch(forms.ModelForm):

    class Meta:
        model=Notice
        fields=('id','date','tender_name')



class InfoOneNoticeSerializer(serializers.ModelSerializer):
    """show the date from the db"""

    class Meta:
        model = Notice
        fields = '__all__'
class MyFilterSet(filters_rest.FilterSet):
    date = filters_rest.DateFilter(
        #distinct= DatePickerInput()
    )

    class Meta:
        model = Notice
        fields = ('id', 'date', 'tender_name')

    # def get_form_class(self):
    #     # widgets = {
    #     #     'date': DatePickerInput(),
    #     # }
    #     return forms


class AllNoticeView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = InfoOneNoticeSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'
    filter_backends = [filters_rest.DjangoFilterBackend]
    filterset_class = MyFilterSet


    def get(self, request):
        search_name = self.request.query_params.get('tender_name', None)
        search_id = self.request.query_params.get('id', None)
        search_date = self.request.query_params.get('date', None)
        queryset = Notice.objects.all()
        if search_name:
            query=queryset.filter(tender_name=search_name)
        elif search_id:
            query=queryset.filter(id=search_id)
        elif search_date:
            query = queryset.filter(date=search_date)
        else:
            query=Notice.objects.all()
        return Response({'notices': query,
                         'filters':MyFilterSet})

    # def get(self, request, format=None):
    #     """
    #     Return a list of all users.
    #     """
    #     notice = [simple.tender_name for simple in Notice.objects.all()]
    #     return Response(notice)


class NoticeListView(api_views.ListAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    #queryset = Notice.objects.all()
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['tender_name','id','date']
    # filterset_fields=['tender_name','id','date']
    # filterset_fields=SearchSerializer
    serializer_class = InfoOneNoticeSerializer
    filter_backends = [filters_rest.DjangoFilterBackend]
    filterset_class=MyFilterSet
    def get_queryset(self,**kwargs):
        search_name = self.request.query_params.get('tender_name', None)
        search_id = self.request.query_params.get('id', None)
        search_date = self.request.query_params.get('date', None)
        queryset=Notice.objects.all()
        if search_name:
            query=queryset.filter(tender_name=search_name)
        elif search_id:
            query=queryset.filter(id=search_id)
        elif search_date:
            query = queryset.filter(date=search_date)
        else:
            query=Notice.objects.all()
        return query


class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)


