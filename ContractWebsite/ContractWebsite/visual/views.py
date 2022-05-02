from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from django.contrib.auth import mixins as auth_mixin
from scrapy.crawler import CrawlerProcess
from ContractWebsite.visual.forms import SearchConditionForm
from ContractWebsite.visual.models import DateModel
from my_scrapy.my_scrapy.spiders.notices import TestSpider
import platform as plt
import os
from ContractWebsite.first.models import Notice


UserModel=get_user_model()

class CreateNewUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username','first_name', 'last_name','password1', 'password2', )


class ViewPage(views.TemplateView):
    template_name = 'index_a.html'

class LogedPage(views.CreateView):
    form_class = SearchConditionForm
    template_name = 'loged.html'
    context_object_name='form'
    success_url = reverse_lazy('logged')




class AdminsPage(auth_mixin.LoginRequiredMixin,views.TemplateView):
    template_name = 'admins.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = UserModel.objects.all()
        context['each_notice'] = Notice.objects.values_list('date', flat=True).distinct()
        return context

class EditUsers(auth_mixin.LoginRequiredMixin,views.edit.UpdateView):
    template_name = 'edit_user.html'
    model = UserModel
    fields = "__all__"
    success_url = reverse_lazy('admins')


class MyLoginView(LoginView):
    template_name = 'index_a.html'
    def get_success_url(self):
        return reverse_lazy('logged')

class LogoutPageView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('index_a')


class RegistrationView(views.CreateView):
    form_class = CreateNewUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('logged')

@login_required()
def delete_user(request,pk):
    user_for_delete=UserModel.objects.get(id=pk)
    user_for_delete.delete()
    return redirect('admins')


class Back(auth_mixin.LoginRequiredMixin,views.TemplateView):
    template_name = 'index_a.html'


def my_crawl_scrapy(request):
    """
     this function start crawling ==> now it is test website
     have to be NoticesSpider(change the name in start.py)
     """
    print('start scrapy function')
    cwd = os.path.join("C:\\Users\\Owner\\Desktop\\Test-Website\\Contract-notices-website\\ContractWebsite\\my_scrapy\\my_scrapy", "start.py")
    os.system('{} {}'.format('python', cwd))
    return redirect('logged')




