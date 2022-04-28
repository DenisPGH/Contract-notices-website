from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics as api_views
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import filters
from django_filters import rest_framework as filters_rest
from django import forms

# Create your views here.
from rest_framework.response import Response

from ContractWebsite.first.models import Notice

class MyDateFilter(filters_rest.DateFilter):
    date = filters_rest.DateFromToRangeFilter()


    # class Meta:
    #     model = Notice
    #     fields = ['id','date','tender_name']

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ('id','date','tender_name')


class FormSearch(forms.ModelForm):
    class Meta:
        model=Notice
        fields=('id','date','tender_name')



class InfoOneNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'

class AllNoticeView(APIView):
    #queryset = Notice.objects.all()
    serializer_class = InfoOneNoticeSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        queryset = Notice.objects.all()
        return Response({'notices': queryset})

    # def get(self, request, format=None):
    #     """
    #     Return a list of all users.
    #     """
    #     notice = [simple.tender_name for simple in Notice.objects.all()]
    #     return Response(notice)



class NoticeListView(api_views.ListAPIView):
    #queryset = Notice.objects.all()
    serializer_class = InfoOneNoticeSerializer
    #filter_backends = [filters.SearchFilter]
    filter_backends = [filters_rest.DjangoFilterBackend]
    search_fields = ['tender_name','id','date']
    filterset_fields=['tender_name','id','date']
    #filterset_fields=SearchSerializer
    #filterset_class=MyDateFilter
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


