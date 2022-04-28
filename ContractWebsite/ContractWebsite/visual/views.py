from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms


# Create your views here.

class CreateNewUserForm(auth_forms.UserCreationForm):

    # first_name = forms.CharField(max_length=25, )
    # last_name = forms.CharField(max_length=30)
    # email = forms.EmailField(
    #     Null=True,
    # )
    #
    #
    # def save(self, commit=True):
    #     user = super().save(commit=commit)
    #     profile = Profile(
    #         first_name=self.cleaned_data['first_name'],
    #         last_name=self.cleaned_data['last_name'],
    #         picture=self.cleaned_data['picture'],
    #         born=self.cleaned_data['born'],
    #         user=user,
    #     )
    #
    #     if commit:
    #         profile.save()
    #         wait_user = WaitingUser(
    #             first_name=self.cleaned_data['first_name'],
    #             last_name=self.cleaned_data['last_name'],
    #             id=profile.pk,
    #
    #         )
    #         wait_user.save()
    #     return user

    class Meta:
        model = get_user_model()
        fields = ('username','first_name', 'last_name','password1', 'password2', )


class ViewPage(views.TemplateView):
    template_name = 'index_a.html'


class MyLoginView(LoginView):
    template_name = 'index_a.html'
    def get_success_url(self):
        return reverse_lazy('filter')
class LogoutPageView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('index_a')
class RegistrationView(views.CreateView):
    form_class = CreateNewUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('filter')