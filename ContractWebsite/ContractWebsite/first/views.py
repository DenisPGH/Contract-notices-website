from django.shortcuts import render
from rest_framework import generics as api_views
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.renderers import TemplateHTMLRenderer

# Create your views here.
from rest_framework.response import Response

from ContractWebsite.first.models import Notice


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
        return Response({'profiles': queryset})

    # def get(self, request, format=None):
    #     """
    #     Return a list of all users.
    #     """
    #     notice = [simple.tender_name for simple in Notice.objects.all()]
    #     return Response(notice)


